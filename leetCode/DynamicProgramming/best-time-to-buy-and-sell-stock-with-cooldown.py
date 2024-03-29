# 309. Best Time to Buy and Sell Stock with Cooldown

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} 
        def dfs(i, buying):
            if i >= len(prices): return 0
            if (i, buying) in dp: return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        return dfs(0, True)

# sol 2:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f1, f2, f3 = -prices[0], 0, 0
        for p in prices[1:]:
            f1, f2, f3 = max(f1, f3 - p), max(f2, f1 + p), max(f3, f2)
        return f2
