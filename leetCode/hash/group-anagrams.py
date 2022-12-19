# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Sol 1: O(m*n log(n))
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = {}

        for i in range(len(strs)):
            sortedStr = ''.join(sorted(strs[i]))
            
            if sortedStr in hashStr:
                hashStr[sortedStr].append(strs[i])
            else:
                hashStr[sortedStr] = [strs[i]]
        
        return hashStr.values()

# Sol 1: O(m*n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStr = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('c')] += 1 
            temp = hashStr.get(tuple(count),[])
            temp.append(s)
            hashStr[tuple(count)] = temp
        
        return hashStr.values()