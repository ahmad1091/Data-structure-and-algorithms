# 25. Reverse Nodes in k-Group

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, k):
        previous, current, next = None, head, None
        index = 0
        while current and index < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            index += 1
        return previous, current, next


    # find_length will find the total length of the linked list
    def find_length(self, start):
        current = start
        count = 0
        while current:
            current = current.next
            count += 1
        return count

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head:
            return head
        i, count = 0, 0
        current, previous = head, None
        total_length = self.find_length(head)
        while True:
            i += 1
            last_node_of_previous_part = previous
            last_node_of_current_part = current
            next = None  
            previous, current, next = self.reverse(last_node_of_current_part, k)
            count += k
            if last_node_of_previous_part:
                last_node_of_previous_part.next = previous
            else:
                head = previous
            last_node_of_current_part.next = current

            if current is None or (total_length - count) < k:
                break
            previous = last_node_of_current_part
        return head