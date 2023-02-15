# 552. Student Attendance Record II

# An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(n, cons, hasA):
            if n == 0: return 1
            temp = 0
            if not hasA:
                temp += dfs(n - 1, 0, True) # adding A
                temp %= MOD
            if cons < 2:
                temp += dfs(n - 1, cons + 1, hasA) # adding b
                temp %= MOD
            temp += dfs(n - 1, 0, hasA)
            temp %= MOD

            return temp
        return dfs(n, 0, False)

# sol 2: DP
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = int(1e9 + 7)
        dp = [[[0, 0], [0, 0], [0, 0]] for _ in range(n)]

        dp[0][0][0] = dp[0][0][1] = dp[0][1][0] = 1
        
        for i in range(1, n):
            dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][1][0] + dp[i - 1][2][0]) % mod
            dp[i][0][1] = (dp[i - 1][0][0] + dp[i - 1][1][0] + dp[i - 1][2][0]) % mod + (dp[i - 1][0][1] + dp[i - 1][1][1] + dp[i - 1][2][1]) % mod
            dp[i][1][0] = dp[i - 1][0][0] % mod
            dp[i][1][1] = dp[i - 1][0][1] % mod
            dp[i][2][0] = dp[i - 1][1][0] % mod
            dp[i][2][1] = dp[i - 1][1][1] % mod
        res = 0
        for i in range(3):
            for j in range(2):
               res += dp[-1][i][j]
               res %= mod
        return res
            