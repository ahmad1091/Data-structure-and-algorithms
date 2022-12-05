# 2095. Delete the Middle Node of a Linked List

# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
            
        if count == 1:
            head = None
            return head
        
        steps = floor(count/2)
        node = head
        while steps-1 > 0:
            steps -= 1
            node = node.next
            
        node.next = node.next.next
            
        return head
            