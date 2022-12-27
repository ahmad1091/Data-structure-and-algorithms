# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

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

# sol 2: More clean sol
class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
   
        for i in range(n-1):
            a, b = a + b, a

        return a