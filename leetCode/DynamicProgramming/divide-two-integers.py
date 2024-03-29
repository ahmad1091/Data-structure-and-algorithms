# 29. Divide Two Integers

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

# Sol 1: Linear solution
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        count = 0

        while(d >= dv):
            d -= dv
            count += 1
        if divisor < 0 and dividend >= 0 or divisor > 0 and dividend <= 0:
            count = - count

        return count 

# Sol 2:
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        count = 0

        while(d >= dv):
            mul = 1
            temp = dv
            while d >= temp:
                d -= temp
                count += mul
                mul += mul
                temp += temp

        if divisor < 0 and dividend >= 0 or divisor > 0 and dividend <= 0:
            count = - count

        return min(2147483647,count) 
