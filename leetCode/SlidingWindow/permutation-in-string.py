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

# Solution 2: hashmap O(n)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count,s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')]  += 1
            s2Count[ord(s2[i]) - ord('a')]  += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0      
        for i in range(len(s1),len(s2)):
            if matches == 26: return True

            index = ord(s2[i]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches +=1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches +=1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26




a = Solution()

print(a.checkInclusion('ahmad','ddahamddd'))