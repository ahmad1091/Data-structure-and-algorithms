# 203. Remove Linked List Elements

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(next = head)
        current = head
        prev = dummyNode
        
        while current:
            next = current.next
            
            if current.val == val:
                prev.next = next
            else:
                prev = current
                
            current = next
        return dummyNode.next