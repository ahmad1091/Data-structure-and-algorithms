# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = None

        while(head):
            node = dummyNode
            dummyNode = ListNode(head.val,node)
            head = head.next

        return dummyNode