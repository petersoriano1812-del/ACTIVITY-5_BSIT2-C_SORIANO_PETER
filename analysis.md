# Analysis

**Why does the linked-list stack push at the head instead of the tail?**
In a singly linked list, each node only knows the node after it, so the head is the only end we can reach and change in constant time. Pushing and popping at the head are just pointer updates, so both are O(1). Popping from the tail would require walking the whole list to find the second-to-last node, making `pop` O(n), which breaks the efficiency expected of a stack.

**Why must the array queue be circular?**
In a plain array queue, every `dequeue` either leaves unusable empty slots at the front or forces all remaining elements to shift left, which makes `dequeue` O(n). Using the modulo operator, the front and rear indices wrap back to index 0, so freed slots are reused and both `enqueue` and `dequeue` stay O(1). A size counter is kept to tell a full queue from an empty one, since `front == rear` is ambiguous in both cases.
