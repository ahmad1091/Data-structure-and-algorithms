# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Solution 1: Bad approach

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) <= 1:
            return s1 in s2
        
        # first check if the s1 letters are exist in s2
        for i in s1:
            if i not in s2:
                return False
            
        # second make sure that the indexs of all letters are in sequanse
        
        indexs = []
        for i in s1:
            indexs.append(s2.index(i))
        if(s2.rfind(s1[0]) not in indexs):
            indexs.append(s2.rfind(s1[0]))
        indexs.sort()
        
        sortedStr =''.join(sorted(s1))
        for i in range(indexs[0],indexs[len(indexs)-1]+1) :
            if ''.join(sorted(s2[i:i+len(s1)])) == sortedStr:
                return True
            
        return False
        
