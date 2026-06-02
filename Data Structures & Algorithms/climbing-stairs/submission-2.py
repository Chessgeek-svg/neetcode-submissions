class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        tempSum, prevStep, prevPrevStep = 1 , 1, 1

        for i in range(n-1):
            tempSum = prevStep + prevPrevStep
            prevPrevStep = prevStep
            prevStep = tempSum
        
        return tempSum
            