#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """
        class Square that defines a square
        Attributes:
            __size (int): private size of square
            __postion (tuple): private position passed
        Methods:
            __init__(self, size=0): initializes instance of the class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
            __init__(self, size=0): initializes instance of the class
            Args:
               size (int): size of the square
               position (tuple): position passed
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
            area(self): returns the current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
            size(self): retrieves the size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
            size(self): sets the size
            Args:
                size (int): size passed
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """
            my_print: prints in stdout the square with the character #
        """
        counter = 0
        for i in range(self.area()):
            if len(self.__position) == 2 and i == 0:
                for y in range(self.position[1]):
                    print()
            if counter == self.size:
                print()
                counter = 0
            if len(self.__position) == 2 and counter == 0:
                for y in range(self.__position[0]):
                    print(' ', end='')
            print('#', end='')
            counter += 1
        print()

    @property
    def position(self):
        """
            position(self): retrieves the position property
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
            position(self, position): sets position
            Args:
                position (int): value to set the position with
        """
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
