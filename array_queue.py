"""array_queue.py - Fixed-capacity circular queue (FIFO).

A size counter (not front == rear) distinguishes empty from full.
"""


class ArrayQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.data = [None] * capacity
        self.front = 0   # index of the front element
        self.size = 0    # number of stored elements

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue into a full queue")
        rear = (self.front + self.size) % len(self.data)  # wrap around
        self.data[rear] = value
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.data[self.front]
        self.data[self.front] = None                       # clear the slot
        self.front = (self.front + 1) % len(self.data)     # wrap around
        self.size = self.size - 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.data[self.front]

    def __str__(self):
        n = len(self.data)
        items = [str(self.data[(self.front + i) % n]) for i in range(self.size)]
        return ("[" + ", ".join(items) + "]  (front -> rear)  "
                f"size={self.size}/{n}  front_index={self.front}  "
                f"raw_array={self.data}")
