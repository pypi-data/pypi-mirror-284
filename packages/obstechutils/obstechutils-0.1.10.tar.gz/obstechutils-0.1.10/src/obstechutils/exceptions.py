import sys
import logging

def logged_exit_excepthook(e_type, e_value, e_traceback, thread):
    logger = logging.getLogger()
    logger.error(f"Error of type {e_type} occurred")
    sys.exit(1)

def silent_exit_excepthook(e_type, e_value, e_traceback, thread):
    sys.exit(1)
