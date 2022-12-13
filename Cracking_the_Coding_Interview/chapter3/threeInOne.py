# Three in One: Describe how you could use a single array to implement three stacks.

# Approach 1: Fixed Division
# We can divide the array in three equal parts and allow the individual stack to grow in that limited space.
# Note: We will use the notation "[" to mean inclusive of an end point and "(" to mean exclusive of an end
# point.
# • For stack 1 , we will use [0, n/3)
# • For stack 2, we will use [n/3, 2n/3)
# • For stack 3, we will use [2n/3, n)

class FixedMultiStack:
    numberOfStacks = 3
    stackCapacity = None
    values = []
    sizes = []

    def __init__ (self, stackSize: int):
        self.stackCapacity = stackSize
        self.values = [0] * (stackSize * self.numberOfStacks)
        self.sizes = [0] * self.numberOfStacks

    def isFull(self, stackNum):
        return sizes[stackNum] == self.stackCapacity
    
    def isEmpty(self, stackNum):
        return sizes[stackNum] == 0
    
    def indexOfTop(stackNum):
        offset = stackNum * self.stackCapacity
        size = self.sizes[stackNum]
        return size + offset - 1
    
    def peek(self, stackNum):
        if self.isEmpty(stackNum): return 'EmptyStackException'
        return self.values[indexOfTop(stackNum)]

    def push(self, stackNum, val):
        if self.isFull(stackNum): return 'FullStackException'
        self.sizes[stackNum] += 1
        self.values[] = val

    def pop(self, stackNum):
        if self.isEmpty(stackNum): return 'EmptyStackException'
        topIndex = indexOfTop(stackNum)
        value = values[topIndex]
        value[topIndex] = 0
        sizes[stackNum] -= 1
        return value
