# Remove Dups: Write code to remove duplicates from an unsorted li nked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        slow = head

        while(slow):
            fast = slow
            while (fast.next):
                if(fast.next.val == slow.val):
                    fast.next = fast.next.next
                else:
                    fast = fast.next
            
            slow = slow.next

        for i in range(6): # this loop is for testing
            print(head.val)
            head = head.next


myNode = ListNode(1 ,ListNode(2, ListNode(2, ListNode(3, ListNode(5, ListNode(3, ListNode(4, ListNode(6))))))))


Solution().deleteDuplicates(myNode)
