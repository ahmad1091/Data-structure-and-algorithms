# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
# starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# sol 1: Recursion
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# sol 2: loop
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

# sol 3: Dynamic Programming "Memoization"
class Solution:
    def fib(self, n: int) -> int:
        def fib(i,memo:List[int]):
            if i <= 1: return i

            if memo[i] == 0:
                memo[i] = fib(i - 1, memo) + fib(i - 2, memo)

            return memo[i]

        return fib(n, [0]*(n+1))