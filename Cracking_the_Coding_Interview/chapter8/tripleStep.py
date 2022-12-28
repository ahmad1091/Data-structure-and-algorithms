# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

# SOL 1: runtime of this algorithm is exponential (roughly O( 3 n )
def countWays(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays(n - 1) + countWays(n - 2) + countWays(n - 3)

# SOL 2: Memoization Solution
def countWays(n):
    memo = [-1] * n + 1
    def countWays(i, m:list[int]):
        if i < 0:
            return 0
        elif i == 0:
            return 1
        else:
            memo[i] = countWays(n - 1) + countWays(n - 2) + countWays(n - 3)
            return memo[i]


        