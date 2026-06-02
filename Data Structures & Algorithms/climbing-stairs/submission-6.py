class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        step1, step2 = 1, 2
        for i in range(n-2):
            temp = step1 + step2
            step1 = step2
            step2 = temp
        return step2
        