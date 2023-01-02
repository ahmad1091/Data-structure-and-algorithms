# 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
            
        hashS = {}
        for i, c in enumerate(pattern):
            if (c in hashS and hashS[c] != s[i]) or  (c not in hashS and s[i] in hashS.values()):
                return False
            hashS[c] = s[i]

        return True