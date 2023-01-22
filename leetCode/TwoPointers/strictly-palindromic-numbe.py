# 2396. Strictly Palindromic Number

# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

# Given an integer n, return true if n is strictly palindromic and false otherwise.

# A string is palindromic if it reads the same forward and backward.

class Solution:
    def findString(self, n: int, b: int) -> str:
        res = ''
        while n > 0:
            dig = n % b
            if dig < 10:
                res += str(dig)
            else:
                res += chr(ord('A') + dig - 10)
            n //= b
        return res[::-1]


    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            string = self.findString(n, i)
            if not string == string [::-1]: return False

        return True
     
