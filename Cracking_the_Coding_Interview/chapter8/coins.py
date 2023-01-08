# Coins: Given an innnite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, a):
            if a == amount: return 1
            if a > amount: return 0
            if i == len(coins): return 0
            if (i, a) in cache: return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]
        
        return dfs(0, 0)

