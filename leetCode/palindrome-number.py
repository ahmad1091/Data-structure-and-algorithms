# 9. Palindrome Number

# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# sol 2: Math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        y, t = 0, x
        while t:
            y = y * 10 + t % 10
            print(y)
            t //= 10
        
        return x == y