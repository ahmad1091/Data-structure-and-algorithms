# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.

class DinnerPlates:
    def __init__(self, capacity: int):
        self.stacks = []
        self.capacity = capacity
        

    def push(self, val: int) -> None:
        last = self.getLastStack()
        if last != None and len(last) < self.capacity:
            last.append(val)
        else:
            stack = []
            stack.append(val)
            self.stacks.append(stack)

    def pop(self) -> int:
        last = self.getLastStack()
        if last == None: return 0
        val = last.pop()
        if len(last) == 0: 
            self.stacks.pop()
        return val

    def popAtStack(self, index: int) -> int:
        return self.leftShift(index, True)
    
    def getLastStack(self) -> List[int]:
        if len(self.stacks) == 0: return None
        return self.stacks[-1]

    def isEmpty(self):
        last = self.getLastStack()
        return last == None or len(last) == 0
    
    def leftShift(self, index: int, removeTop:bool):
        stack = self.stacks[index]
        removeItem = None
        if (removeTop):
            removedItem = stack.pop()
        else:
            removedItem = stack.pop(0)

        if(len(stack) == 0):
            self.stacks.pop(index)

        elif len(self.stacks) > index + 1:
            v = self.leftShift(index + 1, False)
            stack.append(v)
        return removedItem

