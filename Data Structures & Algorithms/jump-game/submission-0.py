class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) -1
        remainingJump = 1
        for i in range(len(nums) -1):
            remainingJump -= 1
            remainingJump = max(remainingJump, nums[i])
            if remainingJump <= 0:
                return False
        return True
