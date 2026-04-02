class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for price in prices:
            # cheapest buy price
            if price < buy:
                buy = price

            max_profit = max(max_profit, price - buy)

        # this way, we do not need to sort
        # time is O(n), space is O(1)
        return max_profit

        # time is O(n) and space is O(1)