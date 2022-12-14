# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returnsD the minimum element? Push, pop and min should all operate in 0(1) time.

class NodeWithMin:
    value = None
    min = int

    def __init__(self, val, min):
        self.value = val
        self.min = min

class StackWithMin(Stack,NodeWithMin):

    def push(self,val):
        newMin = min(value, self.min())
        super.push(new NodeWithMin(value, newMin))

    def min:
        if self.isEmpty: return int('inf')
        else:
            super(Peri, self).display()peek().min




