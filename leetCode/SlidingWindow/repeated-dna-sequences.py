# 187. Repeated DNA Sequences

# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

# sol 1: Brut force
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)):
            print(s[i:i + 10])
            if s[i:i + 10] in s[i + 1:]:
                res.append(s[i:i + 10])
        return list(set(res))

# sol 2:
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res, seen = [], set()

        for l in range(len(s) - 9):
            cur = s[l:l + 10]
            if (cur in seen) and (cur not in res):
                res.append(cur)
            seen.add(cur)
        return res
            