#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if b == 0:
            result = None
        else:
            result = a / b
    except Exception as e:
        print(e, end='')
    finally:
        print("Inside result: {}".format(result))
    return result
