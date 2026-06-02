class Solution:
    def climbStairs(self, n: int) -> int:
        step2, step1 = 1, 1

        for i in range(1, n):
            temp = step1 + step2
            step2 = step1
            step1 = temp
        return step1