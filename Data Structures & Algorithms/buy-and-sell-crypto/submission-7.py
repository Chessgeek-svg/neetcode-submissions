class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = profit = 0
        for sell in range(len(prices)):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
        return profit