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

# or:
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = {}
        res = []

        for i in range(len(s) - 9):
            cur = s[i:i + 10]
            cnt[cur] = 1 + cnt.get(cur, 0)
            if cnt[cur] == 2:
                res.append(cur)
            
        return res

# sol 3: Hashing 
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return set()
        base = 4
        hi_place_value = pow(base, 10)
        mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        numbers = []
        for i in range(len(s)):
            numbers.append(mapping.get(s[i]))
        hashing = 0
        substring_hashes, output = set(), set()
        for start in range(len(s) - 9):
            if start != 0:
                hashing = hashing * base - \
                    numbers[start - 1] * hi_place_value + \
                    numbers[start + 9]
            else:
                for end in range(10):
                    hashing = hashing * base + numbers[end]
            if hashing in substring_hashes:
                output.add(s[start:start + 10])
            substring_hashes.add(hashing)
        return output
            