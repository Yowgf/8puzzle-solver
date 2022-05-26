from contextlib import contextmanager
from copy import copy
from math import sqrt
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

def slen(l):
    return int(sqrt(len(l)))

def swap(l, from_pos, to_pos):
    l = copy(l)
    temp = l[to_pos]
    l[to_pos] = l[from_pos]
    l[from_pos] = temp
    return l

@contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
