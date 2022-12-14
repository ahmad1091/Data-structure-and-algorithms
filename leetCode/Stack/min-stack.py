# 155. Min Stack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:
    min = []

    def __init__(self):
        self.s = []
        self.min = []

    def push(self, val: int) -> None:
        self.s.append(val)
        val = min(val,self.min[-1] if self.min else val)
        self.min.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.min.pop()

    def top(self) -> int:
        return self.s[-1]
    
    def getMin(self) -> int:
        return self.min[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()