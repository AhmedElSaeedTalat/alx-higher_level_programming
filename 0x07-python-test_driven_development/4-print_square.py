#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
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
