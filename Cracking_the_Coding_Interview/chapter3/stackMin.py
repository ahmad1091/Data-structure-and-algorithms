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
            super(NodeWithMin, self).display()peek().min
        

class StackWithMin2(Stack):

    def __init__(self) {
        self.s2 = new Stack()

    def push(self, value):
        if value <= min():
            s2.push(value)
        super(Stack,self).push(value)

    def pop(self):
        value = super(Stack,self).pop()

        if value == min:
            s2.pop()
        
        return value


    def min(self):
        if(self.s2.isEmpty()): return float('inf')
        return self.s2.peek()

    




