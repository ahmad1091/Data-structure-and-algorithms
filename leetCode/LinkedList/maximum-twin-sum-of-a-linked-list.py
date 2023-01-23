# 2130. Maximum Twin Sum of a Linked List

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = [] 
        current = head

        while current:
            arr.append(current.val)
            current = current.next

        n = len(arr)
        return max([arr[i] + arr[n - i - 1] for i in range(n)])

# sol 2: more optimal
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head):
            dummy = ListNode()
            cur = head
            while cur:
                nxt = cur.next
                cur.next = dummy.next
                dummy.next = cur
                cur = nxt
            return dummy.next

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        first = head
        q = slow.next
        slow.next = None
        second = reverse(q)
        res = 0

        while second and first:
            res = max(res, second.val + first.val)
            first = first.next
            second = second.next
        
        return res