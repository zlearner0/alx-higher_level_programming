#!/usr/bin/python3
"""
This is the documentation for the module 100-singly_linked_list.py.
"""


class Node:
    """
    This class defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object

        Args:
            data (int): the node data
            next_node (Node): the next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Returns:
            The node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the node data

        Args:
            value (int): the node data

        Raises:
            TypeError: if value isn't an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Returns:
            The next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list

        Args:
            value (Node): the next node in the linked list

        Raises:
            TypeError: if value isn't None or a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list
    """

    def __init__(self):
        """
        Initializes a new, empty singly linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list

        Args:
            value (int): the value to insert into the linked list
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            crnt = self.head
            while crnt.next_node is not None and crnt.next_node.data < value:
                crnt = crnt.next_node
            new_node.next_node = crnt.next_node
            crnt.next_node = new_node

    def __str__(self):
        """
        Returns:
            A string representation of the linked list
        """
        result = ""

        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node

        return result
