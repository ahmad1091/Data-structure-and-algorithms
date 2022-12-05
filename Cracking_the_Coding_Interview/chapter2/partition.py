# 2.4: Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

# Solution 1: If we don't care about making the elements of the list "stable"

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        start = head 
        end = head 
        
        while head:
            next = head.next
            if(head.val < x):
                head.next = start
                start = head
            else:
                end.next = head
                end = head
            head = next
            
        end.next = None
        
        return start

# Solution 2: If we need to keep the elements stable


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        beforeStart = None
        beforeEnd = None
        afterStart = None
        afterEnd = None

        while head:
            next = head.next
            head.next = None
            if head.val < x:
                if(beforeStart == None):
                    beforeStart = head
                    beforeEnd = beforeStart
                else:
                    beforeEnd.next = head
                    beforeEnd = head
            else:
                if(afterStart == None):
                    afterStart = head
                    afterEnd = afterStart
                else:
                    afterEnd.next = head
                    afterEnd = head
            head = next

        if(beforeStart == None):
            return afterStart

        beforeEnd.next = afterStart

        return beforeStart

        

