"""main.py - Menu-driven program for stacks and queues.

Choose an implementation, then perform any operation. The state of the
structure is printed after every operation. Errors (underflow/overflow)
are reported, never silently ignored.

Run:  python main.py
"""
from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

IMPLEMENTATIONS = {
    "1": ("Array Stack", ArrayStack, "stack", True),
    "2": ("Linked Stack", LinkedStack, "stack", False),
    "3": ("Array Queue (circular)", ArrayQueue, "queue", True),
    "4": ("Linked Queue", LinkedQueue, "queue", False),
}


def read(prompt):
    """input() wrapper: returns None on end-of-input so piped runs stop cleanly."""
    try:
        return input(prompt).strip()
    except EOFError:
        return None


def ask_capacity():
    while True:
        raw = read("Enter capacity (positive integer): ")
        if raw is None:
            return None
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("  Invalid capacity. Try again.")


def run_structure(name, struct, kind):
    if kind == "stack":
        add, remove, look = "Push", "Pop", "Peek"
        add_fn, remove_fn, look_fn = struct.push, struct.pop, struct.peek
    else:
        add, remove, look = "Enqueue", "Dequeue", "Peek front"
        add_fn, remove_fn, look_fn = struct.enqueue, struct.dequeue, struct.peek_front

    print(f"\n--- {name} ---")
    print(f"State: {struct}")
    while True:
        print(f"\n1. {add}  2. {remove}  3. {look}  4. Is empty?  "
              f"5. Is full?  6. Show state  0. Back")
        choice = read("Choose: ")
        if choice is None or choice == "0":
            return choice is not None
        try:
            if choice == "1":
                value = read("  Value to add: ")
                if value is None:
                    return False
                add_fn(value)
                print(f"  {add}ed {value!r}")
            elif choice == "2":
                print(f"  {remove} returned {remove_fn()!r}")
            elif choice == "3":
                print(f"  {look} returned {look_fn()!r}")
            elif choice == "4":
                print(f"  is_empty() = {struct.is_empty()}")
            elif choice == "5":
                print(f"  is_full() = {struct.is_full()}")
            elif choice == "6":
                pass
            else:
                print("  Invalid choice.")
                continue
        except (IndexError, OverflowError) as err:
            print(f"  ERROR: {err}")
        print(f"State: {struct}")


def main():
    while True:
        print("\n===== Stacks and Queues =====")
        for key, (label, _, _, _) in IMPLEMENTATIONS.items():
            print(f"{key}. {label}")
        print("0. Exit")
        choice = read("Choose implementation: ")
        if choice is None or choice == "0":
            print("Goodbye!")
            return
        if choice not in IMPLEMENTATIONS:
            print("Invalid choice.")
            continue
        label, cls, kind, needs_capacity = IMPLEMENTATIONS[choice]
        if needs_capacity:
            capacity = ask_capacity()
            if capacity is None:
                return
            struct = cls(capacity)
        else:
            struct = cls()
        if not run_structure(label, struct, kind):
            return


if __name__ == "__main__":
    main()
