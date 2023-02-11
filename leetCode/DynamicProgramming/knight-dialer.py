# 935. Knight Dialer

# The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

# A chess knight can move as indicated in the chess diagram below:

# We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

# Given an integer n, return how many distinct phone numbers of length n we can dial.

# You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

# As the answer may be very large, return the answer modulo 109 + 7.

 class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        dp = [1] * 10

        for i in range(n - 1):
            temp = [0] * 10

            temp[0] = dp[4] + dp[6]
            temp[1] = dp[6] + dp[8]
            temp[2] = dp[7] + dp[9]
            temp[3] = dp[4] + dp[8]
            temp[4] = dp[0] + dp[3] + dp[9]
            temp[6] = dp[0] + dp[1] + dp[7]
            temp[7] = dp[2] + dp[6]
            temp[8] = dp[1] + dp[3]
            temp[9] = dp[2] + dp[4]

            dp = temp

        return sum(dp) % (10**9 + 7)
