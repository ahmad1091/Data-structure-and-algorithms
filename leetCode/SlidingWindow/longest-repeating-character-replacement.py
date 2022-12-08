# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
#  You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countHash = {}
        maxWindow = 0
        maxFreq = 0
        l = 0 

        for r in range(len(s)):
            countHash[s[r]] = 1 + countHash.get(s[r],0)
            maxFreq = max(maxFreq,countHash[s[r]])
            while (r - l + 1) - maxFreq > k:
                countHash[s[l]] -= 1
                l += 1
            maxWindow = max(maxWindow, r - l + 1)

        return maxWindow