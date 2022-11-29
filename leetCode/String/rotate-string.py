# 796. Rotate String

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        first = goal[0]
        
        for i in range(len(s)):
            if(s[i] == first):
                if(s[i:] == goal[:len(s[i:])] and s[:i] == goal[len(s[i:]):]):
                    return True
            
        return False    