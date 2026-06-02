class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prev2 = 0, 1

        for i in range(n):
            temp = prev + prev2
            prev2 = prev
            prev = temp
        return prev + prev2