# 2177. Find Three Consecutive Integers That Sum to a Given Number

# Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a = num // 3
        b = num % 3
        return [] if b else [a - 1, a, a + 1]