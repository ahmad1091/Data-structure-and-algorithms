# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                leftSub, rightSub = s[l:r], s[l+1:r+1]
                return (leftSub == leftSub[::-1] or rightSub == rightSub[::-1])
            l += 1
            r -= 1
        return True