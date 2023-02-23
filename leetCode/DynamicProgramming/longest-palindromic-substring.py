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

# sol 2/:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def palCheck(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
            return r - l - 1 
        res = ''
        for i in range(n):
            odd = palCheck(i,i)
            even = palCheck(i, i + 1)
            t = max(odd, even)
            if t > len(res):
                rightBound = i - ((t - 1) >> 1)
                leftBound = rightBound + t
                res = s[rightBound: leftBound]

        return res