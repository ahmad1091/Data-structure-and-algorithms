# 160. Intersection of Two Linked Lists

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all,
# return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None 
        count1 = 0
        count2 = 0

        temp1 = headA
        temp2 = headB

        while temp1.next:
            count1 += 1
            temp1 = temp1.next

        while temp2.next:
            count2 += 1
            temp2 = temp2.next
        
        if(temp1 != temp2):
            return None

        fast = headA if count1 >= count2 else headB
        slow = headA if count1 < count2 else headB
        n = abs(count1 - count2)

        while(n):
            fast = fast.next
            n -= 1

        while fast:
            if(fast == slow ):
                return fast
            fast = fast.next
            slow = slow.next