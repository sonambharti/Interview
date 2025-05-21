"""
Find minimum coins to get the target
"""

def minmCoinChange(coins, amount):
    n = len(coins)
    INF = float('inf')

    # dp[i][j] = min coins to make amount j using first i coins
    dp = [[INF] * (amount + 1) for _ in range(n + 1)]

    # Base case: 0 coins needed to make amount 0
    for i in range(n + 1):
        dp[i][0] = 0

    # Fill the table
    for i in range(1, n + 1):  # i coins
        for j in range(1, amount + 1):  # amount j
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][amount] if dp[n][amount] != INF else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print("No. of ways to get the change: ", minmCoinChange(coins, amount))
