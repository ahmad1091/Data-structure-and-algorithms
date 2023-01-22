# 2108. Find First Palindromic String in the Array

# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            l, r = 0, len(words[i]) - 1
            while l < r:
                if words[i][l] != words[i][r]: break
                l += 1
                r -= 1
            if words[i][l] == words[i][r]: return words[i]
        return ''