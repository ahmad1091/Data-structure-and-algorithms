# 143. Reorder List

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        rev = None
        curr = head
        count = 0
        while(curr):
            count +=1
            node = rev
            rev = ListNode(curr.val,node)
            curr = curr.next
        result = ListNode()

        toggle =True
        while(count/2 > 0):
            if(toggle):
                nxt2 = head.next
                head.next = None
                result.next = head
                head = nxt2
                toggle = not toggle
            else:
                nxt3 = rev.next
                rev.next = None
                result.next = rev
                rev = nxt3
                toggle = not toggle
            count -=1

            result = result.next
            
        return result

# solution 2:

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while(second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        second, first = prev, head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
