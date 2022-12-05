# Delete Middle Node: Implement an algorithm to delete a node in the middle (Le., any node but
# the fi rst and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.


# Sol:
# In this problem, you are not given access to the head of the linked list. You only have access to that node.
# The solution is simply to copy the data from the next node over to the current node, and then to delete the
# next node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteNode(n):
        if n== None or n.next == None:
            return False
        next = n.next
        n.val = next.val
        n.next = next.next
        return True

myNode = ListNode(1 ,ListNode(2, ListNode(2, ListNode(3, ListNode(5, ListNode(3, ListNode(4, ListNode(6))))))))
