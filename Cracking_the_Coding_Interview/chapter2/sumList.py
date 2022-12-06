# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addLists(l1, l2, carry):
            if l1 == None and l2 == None and carry:
                return None

            result = ListNode()
            value = carry
            if l1 != None:
                value += l1.val

            if l2 != None:
                value += l2.val

            result.val = value % 10

            if l1 != None or l2 != None:
                a = None if l1 == None else l1.next
                b = None if l2 == None else l2.next
                c = 1 if value >= 10 else 0
                more = addLists(a,b,c)
                print(more)
                result.next = more
            return result
        return addLists(l1, l2,0)