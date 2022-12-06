# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        testList = []

        while(head):
            testList.append(head.val)
            head = head.next
        string = ''.join(str(x) for x in testList)
        testList.reverse()
        return string == ''.join(str(x) for x in testList)