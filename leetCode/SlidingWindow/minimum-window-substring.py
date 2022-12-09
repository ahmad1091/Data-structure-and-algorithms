# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ''

        tHash,sHash = {},{}

        for c in t:
            tHash[c] = tHash.get(c,0) +1

        l = 0
        res, resLen = [-1,-1], float('inf')
        need, have = len(tHash), 0

        for r in range(len(s)):
            c = s[r]
            sHash[c] = sHash.get(c,0) +1

            if c in tHash and sHash[c] == tHash[c]:
                have += 1

            while have == need:
                if r - l +1 < resLen:
                    resLen = r - l + 1
                    res = [l,r]

                sHash[s[l]] -= 1

                if s[l] in tHash and sHash[s[l]] < tHash[s[l]]:
                    have -= 1

                l += 1
        l,r = res
        return s[l:r+1] if resLen != float('inf') else ''

        