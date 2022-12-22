# 69. Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l + 1 < r:
            mid = (l + r) // 2
            if mid == x // mid: return mid
            elif mid * mid < x: l = mid 
            else: r = mid

        return int(r) if r * r == x else int((l + r) /2)
