class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = prices[0]

        for right in prices:
            if right < left:
                left = right
                continue
            if right - left > maxProfit:
                maxProfit = right - left
        return maxProfit
        