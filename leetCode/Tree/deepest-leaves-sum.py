# 1302. Deepest Leaves Sum

# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            res = 0
            for _ in range(len(q)):
                node = q.popleft()
                res += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

# sol 2: using dfs
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = deepest = 0
        def dfs(root,level):
            nonlocal res, deepest
            if not root: return 
            if deepest == level:
                res += root.val
            elif level > deepest:
                deepest = level
                res = root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return res

                