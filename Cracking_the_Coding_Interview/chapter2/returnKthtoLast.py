# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def returnKthtoLast(self, head,k):
        slow = head
        fast = head

        while( k > 0 and fast):
            fast = fast.next
            k-=1

        while(fast):
            fast = fast.next
            slow = slow.next
    return slow

myNode = ListNode(1 ,ListNode(2, ListNode(2, ListNode(3, ListNode(5, ListNode(3, ListNode(4, ListNode(6))))))))
Solution().returnKthtoLast(myNode,5)

