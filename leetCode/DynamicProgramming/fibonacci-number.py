# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
# starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# sol 1: Recursion // Worse performance
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# sol 2: loop // Best performance
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

# sol 3: Top-Down Dynamic Programming "Memoization" // Optimized solution performance from Recursion Sol
class Solution:
    def fib(self, n: int) -> int:
        def fib(i,memo:List[int]):
            if i <= 1: return i

            if memo[i] == 0:
                memo[i] = fib(i - 1, memo) + fib(i - 2, memo)

            return memo[i]

        return fib(n, [0]*(n+1))

# sol 3: Bottom-Up Dynamic Programming // Optimized solution performance from Recursion Sol
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:return n
        memo = [0] * n
        memo[0] = 0
        memo[1] = 1

        for i in range(2,n):
            memo[i] = memo[i - 1] + memo[i -2]
        
        return memo[n -1] + memo[i - 2]