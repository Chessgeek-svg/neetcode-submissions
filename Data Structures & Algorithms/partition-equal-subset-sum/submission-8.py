class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        if sumNums % 2:
            return False
        midpoint = sumNums // 2
        dp = [False] * (midpoint + 1)
        dp[0] = True
        for num in nums:
            for j in range(midpoint, num-1, -1):
                if dp[j-num]:
                    dp[j] = True
        return dp[midpoint]