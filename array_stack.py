"""array_stack.py - Fixed-capacity stack built on a Python list (LIFO)."""


class ArrayStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.data = [None] * capacity  # fixed-size storage
        self.top = -1                  # -1 means the stack is empty

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push onto a full stack")
        self.top = self.top + 1        # move top up first...
        self.data[self.top] = value    # ...then store

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.data[self.top]    # read the top value first
        self.data[self.top] = None     # clear the slot (tidy; not required)
        self.top = self.top - 1        # then move top down
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.data[self.top]

    def __str__(self):
        items = [str(self.data[i]) for i in range(self.top + 1)]
        return "[" + ", ".join(items) + "]  (bottom -> top)  " \
               f"size={self.top + 1}/{len(self.data)}"
