# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resList = ListNode()
        dummy = resList
        carrier = 0
        temp1 = l1
        temp2 = l2
        count1 = 0
        count2 = 0

        while(temp1):
            count1 += 1
            temp1 = temp1.next
        
        while(temp2):
            count2 += 1
            temp2 = temp2.next

        longer = l1 if count1 >= count2 else l2
        shorter = l1 if count1< count2 else l2
 
        while(longer):
            if(shorter):
                sumOf2 = longer.val + shorter.val + carrier
                shorter = shorter.next
            else:
                sumOf2 = longer.val + carrier
            carrier = 0
            if sumOf2 > 9:
                sumOf2 = sumOf2 % 10
                carrier = 1
            dummy.next = ListNode(sumOf2)
            dummy = dummy.next
            longer = longer.next

        if carrier>0:
            dummy.next = ListNode(carrier)
        return resList.next
