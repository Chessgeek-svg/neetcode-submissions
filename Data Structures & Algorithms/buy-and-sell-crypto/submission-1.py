class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        L = 0
        maxProfit = 0

        for R in range(len(prices)):
            if prices[R] <= prices[L]:
                L = R
                continue
            curProfit = prices[R] - prices[L]
            maxProfit = max(maxProfit, curProfit)
        
        return maxProfit

        