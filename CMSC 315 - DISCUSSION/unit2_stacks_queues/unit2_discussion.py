"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # New items are added to the top of the stack, supporting LIFO behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "Cannot pop from an empty stack."
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Peek allows us to view the top item without removing it.
        if self.is_empty():
            return "Stack is empty."
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # New items are added to the rear, preserving FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return "Cannot dequeue from an empty queue."
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Front returns the next value that will be removed.
        if self.is_empty():
            return "Queue is empty."
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding four items to the stack...")
    stack.push("Book")
    stack.push("Notebook")
    stack.push("Tablet")
    stack.push("Laptop")

    print("Current top item:", stack.peek())

    print("\nRemoving items from the stack (LIFO order):")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print("\nAttempting to pop from an empty stack:")
    print(stack.pop())

    print("\nAttempting to peek at an empty stack:")
    print(stack.peek())

    single_stack = Stack()
    single_stack.push("Only Item")

    print("\nTesting a single-item stack:")
    print("Removed:", single_stack.pop())
    print("Is stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding four customers to the queue...")
    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")
    queue.enqueue("Customer 4")

    print("Customer at front of queue:", queue.front())

    print("\nServing customers (FIFO order):")
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print("\nAttempting to dequeue from an empty queue:")
    print(queue.dequeue())

    print("\nAttempting to view the front of an empty queue:")
    print(queue.front())

    single_queue = Queue()
    single_queue.enqueue("Only Customer")

    print("\nTesting a single-item queue:")
    print("Removed:", single_queue.dequeue())
    print("Is queue empty?", single_queue.is_empty())

    # Real-world scenarios
    print("\n=== REAL-WORLD APPLICATIONS ===")
    print("Stack Example: Undo functionality in a text editor.")
    print("Queue Example: Customers waiting in line at a coffee shop.")


if __name__ == "__main__":
    main()
