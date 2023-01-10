# 112. Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        nodesSum = 0
        bol = False
        def dfs(root):
            nonlocal nodesSum, bol
            if not root:return 
            if not root.left and not root.right:
                if nodesSum + root.val == targetSum: bol = True 
            nodesSum += root.val
            dfs(root.left)
            dfs(root.right)
            nodesSum -= root.val 

        dfs(root)
        return bol
