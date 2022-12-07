# 2.7: Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

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

