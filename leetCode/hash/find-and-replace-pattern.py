# 890. Find and Replace Pattern

# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

# Example 2:

# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        patHash = {}
        res =[]
        for i in range(len(pattern)):
            if patHash.get(pattern[i]) != None:
                patHash[pattern[i]].append(i)
            else:
                patHash[pattern[i]] = [i]
                
        refPattern =list(patHash.values())
            
        for word in words:
            hash ={}
            subPattern = []
            for i in range(len(word)):
                if hash.get(word[i]) != None:
                    hash[word[i]].append(i)
                else:
                    hash[word[i]] = [i]
            subPattern = list(hash.values())
            if len(refPattern) != len(subPattern):
                continue
            else:
                checker = True
                for i in range(len(refPattern)):
                    if refPattern[i] != subPattern[i]:
                        checker = False
                        break  
                if checker:
                    res.append(word)
        return res
                