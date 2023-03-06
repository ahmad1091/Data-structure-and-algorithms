# 1721. Swapping Nodes in a Linked List
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 
# sol:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        for _ in range(k - 1):
            fast = fast.next

        first, slow = fast, head
        while fast.next:
            slow, fast = slow.next, fast.next
        second = slow

        first.val, second.val = second.val, first.val

        return head

# sol 2:
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = end = None
        count = 0
        cur = head
        while cur:
            count += 1

            if end:
                end = end.next
            
            if count == k:
                front = cur
                end = head

            cur = cur.next
        front.val, end.val = end.val, front.val

        return head
