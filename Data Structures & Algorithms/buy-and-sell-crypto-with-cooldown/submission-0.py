class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy, sell, no_buy = [0] * len(prices), [0] * len(prices), [0] * len(prices)
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i] = max(max(no_buy[i-1], 0) - prices[i], buy[i-1])
            sell[i] = buy[i-1] + prices[i]
            no_buy[i] = max(no_buy[i-1], sell[i-1])
        return max(sell)