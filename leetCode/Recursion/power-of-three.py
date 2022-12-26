# 326. Power of Three
# 
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# 
# An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        print(n)
        if n <= 0 :
        	return False
        if n == 1:
        	return True
        if n%3 == 0:
        	return self.isPowerOfThree(n/3)
        else:
        	return False