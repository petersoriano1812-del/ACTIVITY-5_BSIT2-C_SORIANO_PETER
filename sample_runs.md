# Sample Runs

All output below was produced by running the programs in this repository.

## 1. Automated test driver (`python test_driver.py`)
```text
=== ArrayStack (capacity 3) ===
  [OK] pop on empty -> IndexError: Stack underflow: cannot pop from an empty stack
  [OK] peek on empty -> IndexError: Stack is empty: nothing to peek
  push A: [A]  (bottom -> top)  size=1/3
  push B: [A, B]  (bottom -> top)  size=2/3
  push C: [A, B, C]  (bottom -> top)  size=3/3
  pop -> C: [A, B]  (bottom -> top)  size=2/3
  peek -> B: [A, B]  (bottom -> top)  size=2/3
  [OK] push on full -> OverflowError: Stack overflow: cannot push onto a full stack
  [OK] pop after emptying -> IndexError: Stack underflow: cannot pop from an empty stack

=== LinkedStack ===
  [OK] pop on empty -> IndexError: Stack underflow: cannot pop from an empty stack
  [OK] peek on empty -> IndexError: Stack is empty: nothing to peek
  push A: [A]  (bottom -> top)  size=1
  push B: [A, B]  (bottom -> top)  size=2
  push C: [A, B, C]  (bottom -> top)  size=3
  pop -> C: [A, B]  (bottom -> top)  size=2
  peek -> B: [A, B]  (bottom -> top)  size=2
  [OK] pop after emptying -> IndexError: Stack underflow: cannot pop from an empty stack

=== ArrayQueue (capacity 3) ===
  [OK] dequeue on empty -> IndexError: Queue underflow: cannot dequeue from an empty queue
  [OK] peek_front on empty -> IndexError: Queue is empty: nothing to peek
  enqueue A: [A]  (front -> rear)  size=1/3  front_index=0  raw_array=['A', None, None]
  enqueue B: [A, B]  (front -> rear)  size=2/3  front_index=0  raw_array=['A', 'B', None]
  enqueue C: [A, B, C]  (front -> rear)  size=3/3  front_index=0  raw_array=['A', 'B', 'C']
  dequeue -> A: [B, C]  (front -> rear)  size=2/3  front_index=1  raw_array=[None, 'B', 'C']
  enqueue D (WRAP-AROUND to index 0): [B, C, D]  (front -> rear)  size=3/3  front_index=1  raw_array=['D', 'B', 'C']
  [OK] enqueue on full -> OverflowError: Queue overflow: cannot enqueue into a full queue
  [OK] dequeue after emptying -> IndexError: Queue underflow: cannot dequeue from an empty queue

=== LinkedQueue ===
  [OK] dequeue on empty -> IndexError: Queue underflow: cannot dequeue from an empty queue
  [OK] peek_front on empty -> IndexError: Queue is empty: nothing to peek
  enqueue A: [A]  (front -> rear)  size=1
  enqueue B: [A, B]  (front -> rear)  size=2
  enqueue C: [A, B, C]  (front -> rear)  size=3
  dequeue -> A: [B, C]  (front -> rear)  size=2
  [OK] dequeue after emptying -> IndexError: Queue underflow: cannot dequeue from an empty queue

=== Circular queue: many wrap-arounds ===
  [OK] 20 enqueues through a 4-slot array stayed in FIFO order

=== Balanced parentheses ===
  [OK] all balanced and unbalanced cases correct

All tests passed.
```

## 2. Application exercises (`python applications.py`)
```text
=== 6a. Balanced parentheses ===
'()'           -> balanced
'([]{})'       -> balanced
'{[()]}'       -> balanced
'(]'           -> NOT balanced
'(()'          -> NOT balanced
'())'          -> NOT balanced
''             -> balanced
'a(b[c]d)e'    -> balanced
'{[}]'         -> NOT balanced

=== 6b. Print queue simulation ===
Enqueued job J101 (5 page(s))
Enqueued job J102 (12 page(s))
Enqueued job J103 (1 page(s))
Enqueued job J104 (8 page(s))

Printing #1: job J101 (5 page(s)) | waited behind 0 job(s) / 0 page(s)
Printing #2: job J102 (12 page(s)) | waited behind 1 job(s) / 5 page(s)
Printing #3: job J103 (1 page(s)) | waited behind 2 job(s) / 17 page(s)
Printing #4: job J104 (8 page(s)) | waited behind 3 job(s) / 18 page(s)

All jobs done. Total pages printed: 26
```

## 3. Menu-driven program (`python main.py`)
Session: Array Stack (capacity 2) with overflow and underflow, then Array Queue (capacity 3) with wrap-around and overflow.
```text

===== Stacks and Queues =====
1. Array Stack
2. Linked Stack
3. Array Queue (circular)
4. Linked Queue
0. Exit
Choose implementation: Enter capacity (positive integer): 
--- Array Stack ---
State: []  (bottom -> top)  size=0/2

1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Value to add:   Pushed 'A'
State: [A]  (bottom -> top)  size=1/2

1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Value to add:   Pushed 'B'
State: [A, B]  (bottom -> top)  size=2/2

1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Value to add:   ERROR: Stack overflow: cannot push onto a full stack
State: [A, B]  (bottom -> top)  size=2/2

1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose: State: [A, B]  (bottom -> top)  size=2/2

1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Pop returned 'B'
State: [A]  (bottom -> top)  size=1/2

1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Pop returned 'A'
State: []  (bottom -> top)  size=0/2

1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   ERROR: Stack underflow: cannot pop from an empty stack
State: []  (bottom -> top)  size=0/2

1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose: 
===== Stacks and Queues =====
1. Array Stack
2. Linked Stack
3. Array Queue (circular)
4. Linked Queue
0. Exit
Choose implementation: Enter capacity (positive integer): 
--- Array Queue (circular) ---
State: []  (front -> rear)  size=0/3  front_index=0  raw_array=[None, None, None]

1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Value to add:   Enqueueed 'X'
State: [X]  (front -> rear)  size=1/3  front_index=0  raw_array=['X', None, None]

1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Value to add:   Enqueueed 'Y'
State: [X, Y]  (front -> rear)  size=2/3  front_index=0  raw_array=['X', 'Y', None]

1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Dequeue returned 'X'
State: [Y]  (front -> rear)  size=1/3  front_index=1  raw_array=[None, 'Y', None]

1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Value to add:   Enqueueed 'Z'
State: [Y, Z]  (front -> rear)  size=2/3  front_index=1  raw_array=[None, 'Y', 'Z']

1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Value to add:   Enqueueed 'W'
State: [Y, Z, W]  (front -> rear)  size=3/3  front_index=1  raw_array=['W', 'Y', 'Z']

1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose:   Value to add:   ERROR: Queue overflow: cannot enqueue into a full queue
State: [Y, Z, W]  (front -> rear)  size=3/3  front_index=1  raw_array=['W', 'Y', 'Z']

1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  6. Show state  0. Back
Choose: 
===== Stacks and Queues =====
1. Array Stack
2. Linked Stack
3. Array Queue (circular)
4. Linked Queue
0. Exit
Choose implementation: Goodbye!
```
