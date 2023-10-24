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
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''
        getting the data attribute
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''
        setting data attribute
        Parameters:
        - value: data input from outside class
        Raise:
        - TypeError: if data input is not integer
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''
        getting the next_node attribute
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        setting next_node attribute
        Parameters:
        - value: data input from outside class
        Raise:
        - TypeError: if data input is object
        '''
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''
    This is the documentation for SinglyLinkedList class.
    class creates a singly linked list
    '''

    def __init__(self):
        """
        Initializes a new Node object
        """
        self.__head = None

    def sorted_insert(self, value):
        '''
        sorting the nodes upon their value ascendingly
        - value: the data integer of the node
        '''
        current = Node(value)

        if self.__head is None:
            self.__head = current
        elif current.data <= self.__head.data:
            current.next_node = self.__head
            self.__head = current
        else:
            h = self.__head
            while (h):
                if h.next_node and h.next_node.data > current.data:
                    current.next_node = h.next_node
                    h.next_node = current
                    break
                elif not h.next_node:
                    h.next_node = current
                    break

                h = h.next_node

    def __str__(self):
        '''
        string method prints the nodes data
        '''
        h = self.__head
        res = ''
        while (h):
            res += str(h.data) + '\n'
            h = h.next_node
        return res
