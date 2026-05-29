class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # 0 coins needed to get an amount of 0

        for a in range(1, amount + 1):
            for coin in coins:
                difference = a - coin
                
                # can use the coin within the amount
                if difference >= 0:
                    dp[a] = min(dp[a], 1 + dp[difference])

        return dp[-1] if dp[-1] != float('inf') else -1