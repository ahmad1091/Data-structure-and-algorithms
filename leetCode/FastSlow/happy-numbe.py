# 202. Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSqr(num):
            res = 0
            while num >0:
                res += (num % 10)**2
                num //= 10
            return res
        slow, fast = n, sumOfSqr(n)
        while True:
            if fast != 1 and fast != slow:
                slow = sumOfSqr(slow)
                fast = sumOfSqr(sumOfSqr(fast))
            elif fast == 1: return True
            else: return False