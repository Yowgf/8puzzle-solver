from contextlib import contextmanager
import os
import sys

STATUS_FAILED = "FAILED"
STATUS_SUCCESS = "SUCCESS"

def file_exists(fpath):
    return os.path.exists(fpath)

def solver_run_result(status, reason=""):
    result = {}
    result['Status'] = status
    if reason != '':
        result['Reason'] = reason
    return result

def between(n, left, right):
    return left <= n and n <= right

@contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
