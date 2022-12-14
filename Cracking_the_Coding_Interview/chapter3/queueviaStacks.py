# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:

    def __init__(self):
        self.stackNewest = []
        self.stackOldest = []

    def size(self):
        return len(self.stackNewest) + len(self.stackOldest)

    def add(self,val):
        self.stackNewest.append(val)

    def shiftStacks(self):
        if len(self.stackOldest) == 0:
            while(self.stackNewest):
                self.stackOldest.append(self.stackNewest.pop())

    def peek(self):
        self.shiftStacks()
        return self.stackOldest[-1]

    def remove(self):
        self.shiftStacks()
        return self.stackOldest.pop()