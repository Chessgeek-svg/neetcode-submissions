class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum % 2:
            return False
        half = numSum // 2        
        dp = [False] * (half + 1)
        dp[0] = True

        for num in nums:
            for i in range(half, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[half]