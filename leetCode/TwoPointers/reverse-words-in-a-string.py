# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        strArr = s.split()

        for i in range(len(strArr)):
            r, l = i, len(strArr) - 1 - i
            if r < l:
                strArr[r], strArr[l] = strArr[l], strArr[r]
            else: break

        return ' '.join(strArr)