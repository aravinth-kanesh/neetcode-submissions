class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        buy_price = prices[0]

        for price in prices[1:]:
            buy_price = min(buy_price, price)
            max_profit = max(max_profit, price - buy_price)

        return max_profit