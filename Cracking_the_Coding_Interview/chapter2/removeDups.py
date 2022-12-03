# Remove Dups: Write code to remove duplicates from an unsorted li nked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# solution 1:
# class Solution:
#     def deleteDuplicates(self, head):
#         slow = head

#         while(slow):
#             fast = slow
#             while (fast.next):
#                 if(fast.next.val == slow.val):
#                     fast.next = fast.next.next
#                 else:
#                     fast = fast.next
            
#             slow = slow.next

#         for i in range(6): # this loop is for testing
#             print(head.val)
#             head = head.next

# solution 2:
class Solution:
    def deleteDuplicates(self, head):
        hashSet = {}
        prev = ListNode(None)
        while(head != None):
            if head.val in hashSet:
                prev.next = head.next
            else:
                hashSet[head.val] = 1
                prev = head
                print(head.val)
            head = head.next

        for i in range(6): # this loop is for testing
            print(prev.val)
            prev = prev.next


myNode = ListNode(1 ,ListNode(2, ListNode(2, ListNode(3, ListNode(5, ListNode(3, ListNode(4, ListNode(6))))))))


Solution().deleteDuplicates(myNode)
