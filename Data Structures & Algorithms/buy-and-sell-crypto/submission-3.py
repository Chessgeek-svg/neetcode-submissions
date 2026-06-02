class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit = 0
        left = 0
        for right in range(1, len(prices)):
            MaxProfit = max(MaxProfit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
        return MaxProfit