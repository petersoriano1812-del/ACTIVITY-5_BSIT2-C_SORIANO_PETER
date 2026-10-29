# Stacks and Queues: Array vs. Linked List

**Course Module 5 – Fundamental Data Structures (Laboratory Activity)**
Name: LASTNAME, FIRSTNAME  |  Section: SECTION

Python implementations of a stack (LIFO) and a queue (FIFO), each built two ways (fixed-size array and singly linked list) from first principles, without using `list.insert(0, x)`, `list.pop(0)`, or `collections.deque`.

## Files

| File | Description |
|---|---|
| `node.py` | `Node` class shared by the linked structures |
| `array_stack.py` | `ArrayStack`: `push`, `pop`, `peek`, `is_empty`, `is_full` (top starts at -1) |
| `linked_stack.py` | `LinkedStack`: push/pop at the head, no fixed capacity |
| `array_queue.py` | `ArrayQueue`: circular queue using modulo and a size counter |
| `linked_queue.py` | `LinkedQueue`: head (front) and tail (rear) references |
| `main.py` | Menu-driven program; prints the structure state after every operation |
| `applications.py` | Balanced-parentheses checker (stack) and print-queue simulation (queue) |
| `test_driver.py` | Automated tests and demonstrations (wrap-around, underflow, overflow) |
| `sample_runs.md` | Captured output of all programs, including error handling |
| `analysis.md` | Written answer to the analysis question |

## Requirements
Python 3.8 or newer. No external packages.

## How to Run

```bash
# Menu-driven program (choose any of the four implementations)
python main.py

# Test driver: asserts correctness and shows underflow/overflow handling
python test_driver.py

# Application exercises: balanced parentheses and print queue
python applications.py
```

### Using the menu
1. Choose an implementation: Array Stack, Linked Stack, Array Queue, or Linked Queue.
2. Array-based structures ask for a capacity first.
3. Pick an operation (push/pop/peek or enqueue/dequeue/peek front, plus `is_empty`, `is_full`, show state).
4. The state is printed after each operation. The array queue also shows its raw array and front index so wrap-around is visible.

### Running each implementation on its own

```python
from array_stack import ArrayStack
s = ArrayStack(3); s.push("A"); print(s.pop())

from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
```

## Error Handling
Errors are never ignored silently; each raises an exception with a descriptive message:

| Condition | Exception |
|---|---|
| `pop`/`peek` on an empty stack | `IndexError` ("Stack underflow..." / "Stack is empty...") |
| `push` on a full `ArrayStack` | `OverflowError` ("Stack overflow...") |
| `dequeue`/`peek_front` on an empty queue | `IndexError` ("Queue underflow..." / "Queue is empty...") |
| `enqueue` on a full `ArrayQueue` | `OverflowError` ("Queue overflow...") |

## Complexity
All stack and queue operations in all four implementations are O(1).

## Design Notes
- `ArrayStack` starts with `top = -1`; `push` increments then stores, `pop` reads then decrements.
- `LinkedStack` works only at the head so `pop` is O(1).
- `ArrayQueue` computes `rear = (front + size) % capacity` and uses `size` (not `front == rear`) to detect empty/full.
- `LinkedQueue` resets `rear` to `None` when the last element is dequeued.

See `analysis.md` for the written analysis and `sample_runs.md` for sample output.
