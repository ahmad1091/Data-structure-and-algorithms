# Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
# of n pairs of parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = [] 

        def backTrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backTrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                backTrack(openN, closeN + 1)
                stack.pop()

        backTrack(0, 0)
        return res