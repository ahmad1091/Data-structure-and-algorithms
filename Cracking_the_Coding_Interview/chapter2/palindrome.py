# Palindrome: Implement a function to check if a linked list is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Solution 1:
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        testList = []

        while(head):
            testList.append(head.val)
            head = head.next
        string = ''.join(str(x) for x in testList)
        testList.reverse()
        return string == ''.join(str(x) for x in testList)

# Solution 2:
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head

        arr = [] 
        while(fast != None and fast.next != None):
            arr.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if (fast != None):
            slow = slow.next

        while slow:
            top = arr.pop()

            if(top != slow.val):
                return False
            slow = slow.next
        
        return True