# 86. Partition List

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
          