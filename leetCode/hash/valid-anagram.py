# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# sol 1:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sHash = Counter(s)
        tHash = Counter(t)
        for key in sHash:
            if sHash[key] != tHash[key]:
                return False
        return True

# sol 2:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sHash = Counter(s)
        tHash = Counter(t)

        return sHash == tHash