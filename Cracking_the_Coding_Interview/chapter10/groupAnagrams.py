# Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
# each other.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('c')] += 1

            hashStr[tuple(count)].append(s)

        return hashStr.values()

