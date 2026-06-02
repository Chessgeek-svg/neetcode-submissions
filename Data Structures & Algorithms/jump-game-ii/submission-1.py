class Solution:
    def jump(self, nums: List[int]) -> int:
        numberOfJumps = [1001] * len(nums)
        numberOfJumps[0] = 0
        for i in range(len(nums)):
            maxJump = nums[i]
            for j in range(i+maxJump, i, -1):
                if j < len(nums):
                    numberOfJumps[j] = min(numberOfJumps[i] + 1, numberOfJumps[j])
                if j == len(nums) - 1:
                    return numberOfJumps[j]
        return 0