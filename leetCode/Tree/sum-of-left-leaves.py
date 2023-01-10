# 404. Sum of Left Leaves

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftLeaves = 0
        def dfs(root):
            nonlocal leftLeaves
            if not root: return 0
            if root.left and not root.left.left and  not root.left.right: 
                leftLeaves += root.left.val
            dfs(root.left)
            dfs(root.right)
            return leftLeaves

        dfs(root) 
        return leftLeaves