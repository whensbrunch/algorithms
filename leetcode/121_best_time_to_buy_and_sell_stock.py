class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        for p in prices:
            if p < lowest:
                lowest = p
            if p - lowest > max_profit:
                max_profit = p - lowest
        return max_profit