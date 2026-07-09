class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for sell in prices[1:]:
            if sell - buy > maxProfit:
                maxProfit = sell - buy
            elif sell < buy:
                buy = sell
        return maxProfit