# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        opens = {'(':')','{':'}','[':']'}
        stack = [] 
        for i, x in enumerate(s):
            if x not in opens:
                if len(stack) > 0 and opens[stack.pop()] == x:
                    continue
                else:
                    return False
            else:
                stack.append(x)
            
        return len(stack) == 0