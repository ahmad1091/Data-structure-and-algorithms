# # 2074. Reverse Nodes in Even Length Groups
# You are given the `head` of a linked list.

# The nodes in the linked list are **sequentially** assigned to **non-empty** groups whose lengths form the sequence of the natural numbers (`1, 2, 3, 4, ...`). The **length** of a group is the number of nodes assigned to it. In other words,

# * The `1st` node is assigned to the first group.
# * The `2nd` and the 3rd nodes are assigned to the second group.
# * The `4th`,` 5th`, and `6th` nodes are assigned to the third group, and so on.
# * Note that the length of the last group may be less than or equal to `1 + the length of the second to last group`.

# Reverse the nodes in each group with an even length, and return the `head` of the modified linked list.

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        l = 2
        while prev.next:
            node = prev
            n = 0
            for _ in range(l):
                if not node.next:
                    break
                node = node.next
                n += 1
            if n % 2:
                prev = node
            else:
                reverse, cur = node.next, prev.next
                for _ in range(n):
                    cur_next = cur.next
                    cur.next = reverse
                    reverse = cur
                    cur = cur_next

                prev_next = prev.next
                prev.next = node
                prev = prev_next

            l += 1
        return head