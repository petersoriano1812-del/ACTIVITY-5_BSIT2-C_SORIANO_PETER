"""test_driver.py - Automated tests and demonstration runs.

Run:  python test_driver.py
Every check uses assert; the script prints sample runs showing normal use,
wrap-around, and error handling (underflow and overflow).
"""
from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import is_balanced


def expect_error(exc_type, fn, label):
    try:
        fn()
    except exc_type as err:
        print(f"  [OK] {label} -> {exc_type.__name__}: {err}")
    else:
        raise AssertionError(f"{label} did not raise {exc_type.__name__}")


def test_stack(name, stack, can_overflow):
    print(f"\n=== {name} ===")
    assert stack.is_empty()
    expect_error(IndexError, stack.pop, "pop on empty")
    expect_error(IndexError, stack.peek, "peek on empty")
    for v in "ABC":
        stack.push(v)
        print(f"  push {v}: {stack}")
    assert stack.peek() == "C"
    assert stack.pop() == "C"
    print(f"  pop -> C: {stack}")
    assert stack.peek() == "B"
    print(f"  peek -> B: {stack}")
    if can_overflow:
        stack.push("X")           # capacity 3: A, B, X -> full
        assert stack.is_full()
        expect_error(OverflowError, lambda: stack.push("Y"), "push on full")
        assert stack.pop() == "X"
    else:
        assert not stack.is_full()
    assert stack.pop() == "B" and stack.pop() == "A"
    assert stack.is_empty()
    expect_error(IndexError, stack.pop, "pop after emptying")


def test_queue(name, queue, can_overflow):
    print(f"\n=== {name} ===")
    assert queue.is_empty()
    expect_error(IndexError, queue.dequeue, "dequeue on empty")
    expect_error(IndexError, queue.peek_front, "peek_front on empty")
    for v in "ABC":
        queue.enqueue(v)
        print(f"  enqueue {v}: {queue}")
    assert queue.peek_front() == "A"
    assert queue.dequeue() == "A"
    print(f"  dequeue -> A: {queue}")
    if can_overflow:
        # capacity 3: front has moved to index 1, so D lands at physical index 0
        queue.enqueue("D")
        print(f"  enqueue D (WRAP-AROUND to index 0): {queue}")
        assert queue.is_full()
        expect_error(OverflowError, lambda: queue.enqueue("E"), "enqueue on full")
    else:
        queue.enqueue("D")
        assert not queue.is_full()
    assert [queue.dequeue() for _ in range(3)] == ["B", "C", "D"]
    assert queue.is_empty()
    expect_error(IndexError, queue.dequeue, "dequeue after emptying")
    # linked queue must reset rear when it empties: enqueue must still work
    queue.enqueue("Z")
    assert queue.dequeue() == "Z"


def test_circular_many_cycles():
    print("\n=== Circular queue: many wrap-arounds ===")
    q = ArrayQueue(4)
    expected = []
    for i in range(20):
        q.enqueue(i)
        expected.append(i)
        if len(expected) > 2:
            assert q.dequeue() == expected.pop(0)
    assert [q.dequeue() for _ in range(len(expected))] == expected
    print("  [OK] 20 enqueues through a 4-slot array stayed in FIFO order")


def test_balanced():
    print("\n=== Balanced parentheses ===")
    good = ["", "()", "([]{})", "{[()]}", "a(b[c]d)e"]
    bad = ["(", ")", "(]", "(()", "())", "{[}]", "]["]
    for s in good:
        assert is_balanced(s), s
    for s in bad:
        assert not is_balanced(s), s
    print("  [OK] all balanced and unbalanced cases correct")


if __name__ == "__main__":
    test_stack("ArrayStack (capacity 3)", ArrayStack(3), True)
    test_stack("LinkedStack", LinkedStack(), False)
    test_queue("ArrayQueue (capacity 3)", ArrayQueue(3), True)
    test_queue("LinkedQueue", LinkedQueue(), False)
    test_circular_many_cycles()
    test_balanced()
    print("\nAll tests passed.")
