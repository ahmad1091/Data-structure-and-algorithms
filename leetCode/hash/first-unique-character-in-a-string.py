# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        charHash = Counter(s)

        for i in range(len(s)):
            if charHash[s[i]] == 1:
                return i
        
        return -1