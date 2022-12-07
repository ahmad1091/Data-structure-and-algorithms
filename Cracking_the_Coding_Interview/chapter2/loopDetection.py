# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1:
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(fast == slow):
                break

        if fast == None or fast.next == None:
            return None

        slow = head
        while(fast != slow):
            slow = slow.next
            fast = fast.next

        return fast