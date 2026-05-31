class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # track min price seen as you iterate through the array
        # update max_profit = max(max_profit, current_price - min_price)
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price

            max_profit = max(max_profit, price - min_price)
        
        return max_profit