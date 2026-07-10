class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumNums = sum(nums)
        if target % 2 != sumNums % 2:
            return 0
        newTarget = (target + sumNums) // 2
        dp = [0] * (newTarget+1)
        dp[0] = 1
        for num in nums:
            for i in range(newTarget, num-1, -1):
                dp[i] += dp[i-num]
        return dp[newTarget]