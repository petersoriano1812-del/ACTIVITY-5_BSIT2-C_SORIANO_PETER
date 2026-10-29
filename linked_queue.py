"""linked_queue.py - Queue built on a singly linked list with head and tail
references, so enqueue (at tail) and dequeue (at head) are both O(1)."""
from node import Node


class LinkedQueue:
    def __init__(self):
        self.front = None  # dequeue from the head
        self.rear = None   # enqueue at the tail
        self.size = 0

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False  # no fixed capacity

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node        # first element is both front and rear
        else:
            self.rear.next = node    # link after the old tail
        self.rear = node             # new node becomes the rear
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:       # queue became empty -> reset rear too
            self.rear = None
        self.size = self.size - 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.front.value

    def __str__(self):
        items = []
        current = self.front
        while current is not None:
            items.append(str(current.value))
            current = current.next
        return "[" + ", ".join(items) + "]  (front -> rear)  " \
               f"size={self.size}"
