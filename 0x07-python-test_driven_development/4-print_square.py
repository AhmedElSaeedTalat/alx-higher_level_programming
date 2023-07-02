#!/usr/bin/python3
""" function to print squares based on size """


def print_square(size):
    """
        def print_square(size): prints squares based on size
        Args:
            size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size == 0:
        return
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            if i > 0:
                print()
            for y in range(size):
                print('#', end='')
        print()
