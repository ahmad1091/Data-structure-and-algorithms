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

# Approach 2: Flexible Divisions
# A second approach is to allow the stack blocks to be flexible in size. When one stack exceeds its initial
# capacity, we grow the allowable capacity and shift elements as necessary.
# We will also design our array to be circular, such that the final stack may start at the end of the array and
# wrap around to the beginning.

class MultiStack:
    # StackInfo is a simple class that holds a set of data about each stack. It does not hold the actual items in the stack.
    # We could have done this with just a bunch of individual variables, but that's messy and doesn't gain us much.
    class StackInfo:
        start = size = capacity = 0
        def __init__ (self, start, capacity):
            self.start = start
            self.capacity = capacity

        # Check if an index on the full array is within the stack boundaries. The
        # stack can wrap around to the start of the array.
        def isWithinStackCapacity(self,index):
            # If outside of bounds of array, return false.
            if index < 0 or index >= len(self.values):
                return False
            # If index wraps around, adjust it.
            contiguousIndex =  index + len(self.values) if index < self.start else index
            end = self.start + self.capacity
            return self.start <= contiguousIndex and contiguousIndex < end
        
        
        def lastCapacityIndex(self):
            return self.adjustIndex(start + capacity - 1)

        def lastElementIndex(self):
            return adjustIndex(start + size - 1)
        
        def isFull(self): return size == capacity

        def isEmpty(self): return size == 0
    
        info = []
        values = []

        def multiStack(self, numberOfStacks, defaultSize):
            # Create metadata for all the stacks.
            info = [None] * numberOfStacks
            for i in range(len(numberOfStacks)):
                info[i] = new StackInfo(defaultSize * i, defaultSize)
            
            values = [None] * (numberOfStacks * defaultSize)
        
        # Push value onto stack num, shifting/expanding stacks as necessary. Throws
        # exception if all stacks are full.

        def push(self, stackNum, value):
            if allStacksAreFull(): return 'FullStackException'
            stack = self.info[stackNum]
            if(stack.isFull()): expand(stackNum)
            # Find the index of the top element in the array + 1, and increment the
            # stack pointer.
            stack.size += 1
            values[stack.lastElementIndex()] = value

        def pop(self,stackNum):
            stack = self.info[stackNum]
            if stack.isEmpty(); return 'EmptyStackException'

            value = self.values[stack.lastElementIndex()]
            self.values[stack.lastElementIndex()] = 0
            stack.size -= 1
            return value

        def peek(stackNum):
            stack = self.info[stackNum]
            return self.values[stack.lastElementIndex()]
        
        # Shift items in stack over by one element. If we have available capacity, then
        # we'll end up shrinking the stack by one element. If we don't have available
        # capacity, then we'll need to shift the next stack over too.

        def shift(stackNum):
            stack = info[stackNum]
            # If this stack is at its full capacity, then you need to move the next
            # stack over by one element. This stack can now claim the freed index.
            if (stack.size >= stack.capacity):
                nextStack = (stackNum + 1) % len(self.info)
                self.shift(nextStack)
                stack.capacity += 1

            # Shift all elements in stack over by one .
            index = stack.lastCapacityIndex()
            while (stack.isWithinStackCapacity(index)):
                values[index] = values[previousIndex(index)]
                index = previousIndex(index)
            
            # Adjust stack data.
            values[stack.start] = 0 # Clear item
            stack. start = nextIndex(stack.start)# move start
            stack.capacity -= 1 # Shrink capacity

        # Expand stack by shifting over other stacks
        def expand(stackNum):
            shift((stackNum + 1) % info.length)
            info[stackNum].capacity += 1

        # Returns the number of items actually present in stack.
        def numberOfElements():
            size = 0
            for i in info:
                size += i.size
            return size

        # Returns true is all the stacks are full.
        def allStacksAreFull() {
            return numberOfElements() == values.length

        # Adjust index to be within the range of 0 -> length - 1.
        def adjustIndex(index):
            # Java's mod operator can return neg values . For example, (-11 % 5) will
            # return -1, not 4. We actually want the value to be 4 (since we're wrapping
            # around the index).
            max = len(values)
            return ((index % max) + max) % max

        # Get index after this index, adjusted for wrap around.
        def nextIndex(index):
            return self.adjustIndex(index + 1)

        # Get index before this index, adjusted for wrap around.
        def previousIndex(index):
            return self.adjustIndex(index - l)