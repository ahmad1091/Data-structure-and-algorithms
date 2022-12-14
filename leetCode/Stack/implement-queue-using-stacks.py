# 232. Implement Queue using Stacks

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

class MyQueue:

    def __init__(self):
        self.stackNewest = []
        self.stackOldest = []

    def push(self, x: int) -> None:
        self.stackNewest.append(x)

    def pop(self) -> int:
        self.shiftStacks()
        return self.stackOldest.pop()

    def peek(self) -> int:
        self.shiftStacks()
        return self.stackOldest[-1]

    def empty(self) -> bool:
        return len(self.stackNewest) + len(self.stackOldest) == 0

    def shiftStacks(self):
        if len(self.stackOldest) == 0:
            while(self.stackNewest):
                self.stackOldest.append(self.stackNewest.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()