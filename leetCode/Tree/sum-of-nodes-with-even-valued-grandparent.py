# 1315. Sum of Nodes with Even-Valued Grandparent

# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

# A grandparent of a node is the parent of its parent if it exists.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = [0]
        def dfs(root, child):
            if not child:return
            if root.val % 2 == 0:
                if child.left:
                    total[0] += child.left.val
                if child.right:
                    total[0] += child.right.val
            dfs(child, child.left)
            dfs(child, child.right)
        dfs(root, root.left)
        dfs(root, root.right)
        return total[0]