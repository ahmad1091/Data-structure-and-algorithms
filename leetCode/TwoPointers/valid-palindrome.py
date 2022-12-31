# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# sol 1: trivial
class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = ''
        for l in s:
            if l.isalpha() or l.isnumeric():
                modified += l.lower()
        return modified == modified[::-1]

# sol 2: recursion
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def toChar(s: str) -> str:
            res = ''
            for c in s.lower():
                if c.isalpha() or c.isnumeric():
                    res += c
            return res     

        def isPal(s: str) -> bool:
            if len(s) <= 1:
                return True
            else:
                return s[0] == s[-1] and isPal(s[1:-1])

        return isPal(toChar(s))

# sol 3: towPointer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod = ''
        for c in s.lower():
            if c.isalpha() or c.isnumeric():
               mod += c
               
        l, r = 0, len(mod) - 1
        while l < r:
            if mod[l] != mod[r]:
                return False
            l += 1
            r -= 1
        return True