# 895. Maximum Frequency Stack

# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

# Implement the FreqStack class:

# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

# sol 1: 
class FreqStack:
    def __init__(self):
        self.count = {}
        self.bucket = {}
        self.mx = 0

    def push(self, val: int) -> None:
        counter = self.count.get(val, 0) + 1
        self.count[val] =  counter
        if counter > self.mx:
           self.mx = counter 
           self.bucket[counter] = [] 
        self.bucket[counter].append(val)

    def pop(self) -> int:
        val = self.bucket[self.mx].pop()
        self.count[val] -= 1
        if not self.bucket[self.mx]:
            self.mx -= 1
        return val