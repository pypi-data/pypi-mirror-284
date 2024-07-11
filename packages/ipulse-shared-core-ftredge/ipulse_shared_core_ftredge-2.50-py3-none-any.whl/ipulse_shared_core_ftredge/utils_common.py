# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=logging-fstring-interpolation
# pylint: disable=line-too-long
import traceback
import json
import os
import time
from datetime import datetime, timezone
from contextlib import contextmanager
from typing import List
from ipulse_shared_core_ftredge.enums.enums_common_utils import NoticeSeverity
from ipulse_shared_core_ftredge.utils_gcp import write_data_to_gcs

def create_notice(severity, e=None, e_type=None, e_message=None, e_traceback=None, subject=None, message=None,context=None):
    # Validate input: ensure severity is provided, use a default if not
    if severity is None:
        severity = NoticeSeverity.UNKNOWN  # Assume Severity.UNKNOWN is a default fallback

    # If an exception object is provided, use it to extract details
    if e is not None:
        e_type = type(e).__name__ if e_type is None else e_type
        e_message = str(e) if e_message is None else e_message
        e_traceback = traceback.format_exc() if e_traceback is None else e_traceback
    else:
        # Calculate traceback if not provided and if exception details are partially present
        if e_traceback is None and (e_type or e_message):
            e_traceback = traceback.format_exc()

    # Prepare the base notice dictionary with all fields
    notice = {
        "severity_code": severity.value,
        "severity_name": severity.name,
        "subject": subject,
        "message": message,
        "exception_code": e_type,
        "exception_message": e_message,
        "exception_traceback": e_traceback or None,  # Ensure field is present even if traceback isn't calculated
        "context": context or ""
    }
    return notice




def merge_notices_dicts(dict1, dict2):
    """
    Merge two dictionaries of lists, combining lists for overlapping keys.

    Parameters:
    dict1 (dict): The first dictionary of lists.
    dict2 (dict): The second dictionary of lists.

    Returns:
    dict: A new dictionary with combined lists for overlapping keys.
    """
    merged_dict = {}

    # Get all unique keys from both dictionaries
    all_keys = set(dict1) | set(dict2)

    for key in all_keys:
        # Combine lists from both dictionaries for each key
        merged_dict[key] = dict1.get(key, []) + dict2.get(key, [])

    return merged_dict


# ["data_import","data_quality", "data_processing","data_general","data_persistance","metadata_quality", "metadata_processing", "metadata_persistance","metadata_general"]

class Notice:
    def __init__(self, severity: NoticeSeverity, e: Exception = None, e_type: str = None, e_message: str = None, e_traceback: str = None, subject: str = None, message: str = None, context: str = None):
   
        # If an exception object is provided, use it to extract details
        if e is not None:
            e_type = type(e).__name__ if e_type is None else e_type
            e_message = str(e) if e_message is None else e_message
            e_traceback = traceback.format_exc() if e_traceback is None else e_traceback
         # If exception details are provided but not from an exception object
        elif e_traceback is None and (e_type or e_message):
            e_traceback = traceback.format_exc()

        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.severity = severity
        self.subject = subject
        self.message = message
        self.context = context
        self.exception_type = e_type
        self.exception_message = e_message
        self.exception_traceback = e_traceback

    def to_dict(self):
        return {
            "context": self.context,
            "severity_code": self.severity.value,
            "severity_name": self.severity.name,
            "subject": self.subject,
            "message": self.message,
            "exception_type": self.exception_type,
            "exception_message": self.exception_message,
            "exception_traceback": self.exception_traceback,
        }

class NoticesManager:
    ERROR_CODE_START_VALUE = 500

    def __init__(self):
        self.notices = []
        self.error_count = 0
        self.severity_counts = {severity.name: 0 for severity in NoticeSeverity}
        self.context_stack = []

    @contextmanager
    def notice_context(self, context):
        self.push_context(context)
        try:
            yield
        finally:
            self.pop_context()

    def push_context(self, context):
        self.context_stack.append(context)

    def pop_context(self):
        if self.context_stack:
            self.context_stack.pop()

    def get_notices_by_context(self, context_substring: str):
        return [
            notice for notice in self.notices
            if context_substring in notice["context"]
        ]

    def get_current_context(self):
        return " >> ".join(self.context_stack)

    def get_all_notices(self):
        return self.notices
    def add_notice(self, notice: Notice):
        notice.context = self.get_current_context()
        notice_dict = notice.to_dict()
        self.notices.append(notice_dict)
        self._update_counts(notice_dict)

    def add_notices(self, notices: List[Notice]):
        for notice in notices:
            notice.context = self.get_current_context()
            notice_dict = notice.to_dict()
            self.notices.append(notice_dict)
            self._update_counts(notice_dict)
   
    def remove_notice(self, notice: Notice):
        notice_dict = notice.to_dict()
        if notice_dict in self.notices:
            self.notices.remove(notice_dict)
            self._update_counts(notice_dict, remove=True)

    def clear_notices(self):
        self.notices = []
        self.error_count = 0
        self.severity_counts = {severity.name: 0 for severity in NoticeSeverity}

    def contains_errors(self):
        return self.error_count > 0

    def count_errors(self):
        return self.error_count

    def count_notices_by_severity(self, severity: NoticeSeverity):
        return self.severity_counts.get(severity.name, 0)
    
    def count_errors_for_current_context(self):
        current_context = self.get_current_context()
        return sum(
            1 for notice in self.notices
            if notice["context"] == current_context and notice["severity_code"] >= self.ERROR_CODE_START_VALUE
        )
    def count_all_notices(self):
        return len(self.notices)

    def count_notices_for_current_context(self):
        current_context = self.get_current_context()
        return sum(
            1 for notice in self.notices
            if notice["context"] == current_context
        )
    
    def count_notices_by_severity_for_current_context(self, severity: NoticeSeverity):
        current_context = self.get_current_context()
        return sum(
            1 for notice in self.notices
            if notice["context"] == current_context and notice["severity_code"] == severity.value
        )
    def count_notices_for_current_and_nested_contexts(self):
        current_context = self.get_current_context()
        return sum(
            1 for notice in self.notices
            if current_context in notice["context"]
        )
    def count_errors_for_current_and_nested_contexts(self):
        current_context = self.get_current_context()
        return sum(
            1 for notice in self.notices
            if current_context in notice["context"] and notice["severity_code"] >= self.ERROR_CODE_START_VALUE
        )
    def count_notices_by_severity_for_current_and_nested_contexts(self, severity: NoticeSeverity):
        current_context = self.get_current_context()
        return sum(
            1 for notice in self.notices
            if current_context in notice["context"] and notice["severity_code"] == severity.value
        )
    
    def export_notices_to_gcs_file(self, bucket_name, storage_client, file_name=None, top_level_context=None, save_locally=False, local_path=None, logger=None, max_retries=2):
        def log_message(message):
            if logger:
                logger.info(message)

        def log_error(message, exc_info=False):
            if logger:
                logger.error(message, exc_info=exc_info)

        if not file_name:
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            if top_level_context:
                file_name = f"notices_{timestamp}_{top_level_context}_len{len(self.notices)}.json"
            else:
                file_name = f"notices_{timestamp}_len{len(self.notices)}.json"

        cloud_path = None  # Initialize cloud_path here
        local_path = None  # Initialize local_path here
        try:
            cloud_path, local_path = write_data_to_gcs(
                bucket_name=bucket_name,
                storage_client=storage_client,
                data=self.notices,
                file_name=file_name,
                save_locally=save_locally,
                local_path=local_path,
                logger=logger,
                max_retries=max_retries
            )
            log_message(f"Notices successfully saved to GCS at {cloud_path} and locally at {local_path}.")
        except Exception as e:
            log_error(f"Failed to export notices: {type(e).__name__} - {str(e)}", exc_info=True)

        return cloud_path , local_path

    def import_notices_from_json(self, json_or_file, logger=None):
        def log_message(message):
            if logger:
                logger.info(message)
            else:
                print(message)

        def log_error(message, exc_info=False):
            if logger:
                logger.error(message, exc_info=exc_info)
            else:
                print(message)
        try:
            if isinstance(json_or_file, str):  # Load from string
                imported_notices = json.loads(json_or_file)
            elif hasattr(json_or_file, 'read'):  # Load from file-like object
                imported_notices = json.load(json_or_file)
            self.add_notice(imported_notices)
            log_message("Successfully imported notices from json.")
        except Exception as e:
            log_error(f"Failed to import notices from json: {type(e).__name__} - {str(e)}", exc_info=True)

    def _update_counts(self, notice, remove=False):
        if remove:
            if notice["severity_code"] >= self.ERROR_CODE_START_VALUE:
                self.error_count -= 1
            self.severity_counts[notice["severity_name"]] -= 1
        else:
            if notice["severity_code"] >= self.ERROR_CODE_START_VALUE:
                self.error_count += 1
            self.severity_counts[notice["severity_name"]] += 1


class SuccessLog:
    def __init__(self, subject:str, description:str=None, context:str=None):
        self.context = context
        self.subject = subject
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.description = description

    def to_dict(self):
        return {
            "context": self.context or "",
            "subject": self.subject,
            "timestamp": self.timestamp,
            "description": self.description or ""
        }


class SuccessLogManager:
    def __init__(self):
        self.successlogs = []
        self.context_stack = []

    @contextmanager
    def successlog_context(self, context):
        self.push_context(context)
        try:
            yield
        finally:
            self.pop_context()

    def push_context(self, context):
        self.context_stack.append(context)

    def pop_context(self):
        if self.context_stack:
            self.context_stack.pop()

    def get_current_context(self):
        return " >> ".join(self.context_stack)

    def get_all_successlogs(self):
        return self.successlogs

    def add_successlog(self, successlog: SuccessLog):
        successlog.context = self.get_current_context()
        successlog_dict = successlog.to_dict()
        self.successlogs.append(successlog_dict)

    def add_successlogs(self, successlogs: List[SuccessLog]):
        for successlog in successlogs:
            successlog.context = self.get_current_context()
            successlog_dict = successlog.to_dict()
            self.successlogs.append(successlog_dict)

    def remove_successlog(self, successlog: SuccessLog):
        successlog_dict = successlog.to_dict()
        if successlog_dict in self.successlogs:
            self.successlogs.remove(successlog_dict)

    def clear_successlogs(self):
        self.successlogs = []

    def count_all_successlogs(self):
        return len(self.successlogs)

    def count_successlogs_for_current_context(self):
        current_context = self.get_current_context()
        return sum(
            1 for successlog in self.successlogs
            if successlog["context"] == current_context
        )

    def count_successlogs_for_current_and_nested_contexts(self):
        current_context = self.get_current_context()
        return sum(
            1 for successlog in self.successlogs
            if current_context in successlog["context"]
        )


    def export_successlogs_to_gcs_file(self, bucket_name, storage_client, file_name=None, top_level_context=None, save_locally=False, local_path=None, logger=None, max_retries=3):
        def log_message(message):
            if logger:
                logger.info(message)

        def log_error(message, exc_info=False):
            if logger:
                logger.error(message, exc_info=exc_info)

        if not file_name:
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            if top_level_context:
                file_name = f"successlogs_{timestamp}_{top_level_context}_len{len(self.successlogs)}.json"
            else:
                file_name = f"successlogs_{timestamp}_len{len(self.successlogs)}.json"

        cloud_path=None
        local_path=None
        try:
            cloud_path, local_path = write_data_to_gcs(
                bucket_name=bucket_name,
                storage_client=storage_client,
                data=self.successlogs,
                file_name=file_name,
                save_locally=save_locally,
                local_path=local_path,
                logger=logger,
                max_retries=max_retries
            )
            log_message(f"Success logs successfully saved to GCS at {cloud_path} and locally at {local_path}.")
        except Exception as e:
            log_error(f"Failed to export success logs: {type(e).__name__} - {str(e)}", exc_info=True)

        return cloud_path, local_path
    
    def import_successlogs_from_json(self, json_or_file, logger=None):
        def log_message(message):
            if logger:
                logger.info(message)
            else:
                print(message)

        def log_error(message, exc_info=False):
            if logger:
                logger.error(message, exc_info=exc_info)
            else:
                print(message)
        try:
            if isinstance(json_or_file, str):  # Load from string
                imported_success_logs = json.loads(json_or_file)
            elif hasattr(json_or_file, 'read'):  # Load from file-like object
                imported_success_logs = json.load(json_or_file)
            self.add_successlog(imported_success_logs)
            log_message("Successfully imported success logs from json.")
        except Exception as e:
            log_error(f"Failed to import success logs from json: {type(e).__name__} - {str(e)}", exc_info=True)