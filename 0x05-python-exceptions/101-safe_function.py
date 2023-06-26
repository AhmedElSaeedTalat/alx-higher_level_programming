#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(args[0], args[1])
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        return None
    else:
        return result
