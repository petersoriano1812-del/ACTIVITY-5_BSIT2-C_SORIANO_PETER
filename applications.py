"""applications.py - Pair-work application exercises.

6a. Balanced-parentheses checker using a stack.
6b. Print-queue simulation using a queue.
"""
from linked_stack import LinkedStack
from linked_queue import LinkedQueue


def is_balanced(text):
    """Return True if every ( [ { in text is closed by the matching ) ] }
    in the correct order. Characters other than brackets are ignored."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = LinkedStack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False  # closer with no opener, or wrong type
    return stack.is_empty()   # leftover openers mean unbalanced


def simulate_print_queue(jobs):
    """jobs: list of (job_id, pages). Enqueue all, then dequeue and 'print'
    in FIFO order, reporting the wait order."""
    queue = LinkedQueue()
    for job_id, pages in jobs:
        queue.enqueue((job_id, pages))
        print(f"Enqueued job {job_id} ({pages} page(s))")
    print()
    position = 0
    pages_before = 0
    while not queue.is_empty():
        job_id, pages = queue.dequeue()
        position += 1
        print(f"Printing #{position}: job {job_id} ({pages} page(s)) | "
              f"waited behind {position - 1} job(s) / {pages_before} page(s)")
        pages_before += pages
    print(f"\nAll jobs done. Total pages printed: {pages_before}")


if __name__ == "__main__":
    print("=== 6a. Balanced parentheses ===")
    tests = ["()", "([]{})", "{[()]}", "(]", "(()", "())", "", "a(b[c]d)e", "{[}]"]
    for t in tests:
        print(f"{t!r:14} -> {'balanced' if is_balanced(t) else 'NOT balanced'}")

    print("\n=== 6b. Print queue simulation ===")
    simulate_print_queue([("J101", 5), ("J102", 12), ("J103", 1), ("J104", 8)])
