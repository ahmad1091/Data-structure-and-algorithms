# 897. Increasing Order Search Tree

# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(val = 0, right = root)
        prev = dummy
        def dfs(root):
            nonlocal prev
            if not root: return
            dfs(root.left)
            prev.right = root
            root.left = None
            prev = root
            dfs(root.right)

        dfs(root)
        return dummy.right
        