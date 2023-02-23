# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

# sol 1: brut force

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        res = ''
        for i in range(n):
            l = r = i 
            while r < n:
                subStr = s[l:r + 1]
                if subStr == subStr[::-1] and r - l + 1 > len(res):
                    res = s[l:r + 1]
                r += 1
        return res