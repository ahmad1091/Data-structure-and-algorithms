# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength
