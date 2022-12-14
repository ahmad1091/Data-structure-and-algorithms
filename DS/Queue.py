class Queue:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    head = None
    tail = None

    def __init__(self,val=0):
        self.head = new ListNode(val)
        self.tail = head

    def isEmpty(self):
        return self.head == None

    def peek(self):
        return head.val
    
    def add(self,data):
        node = new ListNode(data)

        if tail != None:
            tail.next = node

        tail = node

        if head != None:
            head = node
    
    def remove(self):
        val = head.data
        head = head.next

        if head = None:
            tail = None
        
        return val
        


    

