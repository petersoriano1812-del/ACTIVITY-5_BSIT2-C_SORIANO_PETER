"""linked_stack.py - Stack built on a singly linked list (no fixed capacity).

push and pop both work at the HEAD of the list, so both are O(1).
"""
from node import Node


class LinkedStack:
    def __init__(self):
        self.top = None  # head of the list = top of the stack
        self.size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False  # a linked stack only runs out when memory does

    def push(self, value):
        node = Node(value)
        node.next = self.top   # new node points to the old top
        self.top = node        # new node becomes the top
        self.size = self.size + 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next  # move top down the chain
        self.size = self.size - 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.top.value

    def __str__(self):
        items = []
        current = self.top
        while current is not None:
            items.append(str(current.value))
            current = current.next
        items.reverse()  # list was walked top -> bottom; show bottom -> top
        return "[" + ", ".join(items) + "]  (bottom -> top)  " \
               f"size={self.size}"
