class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        if sumNums % 2:
            return False
        mid = sumNums // 2
        dp = [False] * (mid + 1)
        dp[0] = True
        for num in nums:
            for i in range(mid, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[mid]