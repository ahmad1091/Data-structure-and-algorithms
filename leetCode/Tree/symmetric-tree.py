# 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(lRoot, rRoot):
            if not lRoot and not rRoot:
                return True
            if not lRoot or not rRoot or lRoot.val != rRoot.val:
                return False
            return dfs(lRoot.left,rRoot.right) and dfs(lRoot.right,rRoot.left)

        return dfs(root, root)

                        