#!/usr/bin/python3
""" class Node that defines a node of a singly linked list """


class Node:
    """ class Node that defines a node of a singly linked list
        Attributes:
            __data (int): private int representing data of each node
            __next_node: private Node
        Methods:
            __init__(self, data, next_node=None): initializes instance
            of a class
    """

    def __init__(self, data, next_node=None):
        """__init__(self, data, next_node=None):
           initializes instance of a class
           Args:
               data (int): data of each node
               next_node (): node passed
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """ data(self): retrieves data """
        return self.__data

    @data.setter
    def data(self, value):
        """ data(self): sets data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ next_node(self): retrieves next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next_node(self): sets next_node """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


""" class Node that defines a node of a singly linked list """


class SinglyLinkedList:
    """ class SinglyLinkedList that defines a node of a singly linked list
        Attributes:
            head (int): private head
        Methods:
            __init__(self): initializes instance of a class
    """
    def __init__(self):
        """ __init__(self): initializes instance of a class """
        self.__head = None

    def __str__(self):
        if self.__head is None:
            return ''
        current = self.__head
        l_list = []
        while current:
            l_list.append(str(current.data))
            current = current.next_node
        return '\n'.join(l_list)

    def sorted_insert(self, value):
        """ insert new node """
        new_node = Node(value)
        current = self.__head
        i = 0
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        else:
            while current:
                if value < current.data and i == 0:
                    new_node.next_node = current
                    self.__head = new_node
                    break
                elif value > current.data and current.next_node is None:
                    current.next_node = new_node
                    new_node.next_node = None
                    break
                elif value >= current.data and value < current.next_node.data:
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    break
                i += 1
                current = current.next_node
