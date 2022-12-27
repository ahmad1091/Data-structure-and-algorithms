# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# sol 1: Top-Down Dynamic Programming "Memoization"
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:return n
        dp = [0] * n
        dp[n - 1] = 1
        dp[n - 2] = 1
        for i in range(n -3, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]

        print(dp)
        return dp[0]

# sol 2: Top-Down Dynamic Programming "Memoization" cleaner Code
class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
   
        for i in range(n-1):
            a, b = a + b, a

        return a

# sol 3: Bottom-Up Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        def climbStairs(i, memo:list[int]):
            if i <= 2: return i

            if memo[i] == 0:
                memo[i] = climbStairs(i - 1, memo) + climbStairs(i - 2, memo)

            return memo[i]

        return climbStairs(n, [0]*(n+1))