# 987. Vertical Order Traversal of a Binary Tree

# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(root, r, c):
            if not root: return 
            res.append((r, c, root.val))
            dfs(root.left, r + 1, c - 1)
            dfs(root.right, r + 1, c + 1)
            return 
        dfs(root, 0, 0)
        sortedRes = sorted(res, key = lambda x:(x[1], x[0], x[2]))
        ans = []
        cur = None
        for r, c, v in sortedRes:
            if c != cur:
                ans.append([v])
                cur = c
                continue
            ans[-1].append(v)
        return ans
