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

# slo 2: using arr
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

# sol 3: reverse whole LinkedList
class Solution:
    def reverseAndClone(self, head: Optional[ListNode]) -> [ListNode]:
        node = None
        while(head):
            n = ListNode(head.val)
            n.next = node
            node = n
            head = head.next
        return node

    def isEqual(self,one : [ListNode],two:[ListNode]) -> bool:
        while (one and two):
            if one.val != two.val:
                return False
            one = one.next
            two = two.next
        return one == None and two == None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed = self.reverseAndClone(head)
        return self.isEqual(head, reversed)

# sol 4: reverse half linkedList
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        
        while second and first:
            if(second.val != first.val):return False
            first = first.next
            second = second.next
        return True