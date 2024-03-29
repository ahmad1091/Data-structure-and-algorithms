# 783. Minimum Distance Between BST Nodes

# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = prev = inf
        def dfs(root):
            if not root:
                return 
            nonlocal res, prev
            dfs(root.left)
            res = min(res, abs(prev - root.val))
            prev = root.val
            dfs(root.right)
        
        dfs(root)
        return res