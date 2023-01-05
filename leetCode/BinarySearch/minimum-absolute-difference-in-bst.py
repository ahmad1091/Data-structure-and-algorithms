# 530. Minimum Absolute Difference in BST

# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = prev = inf

        def dfs(root):
            if root is None:
                return 
            dfs(root.left)
            nonlocal ans ,prev
            ans = min(ans, abs(prev - root.val))
            prev = root.val
            dfs(root.right)

        dfs(root)
        return ans