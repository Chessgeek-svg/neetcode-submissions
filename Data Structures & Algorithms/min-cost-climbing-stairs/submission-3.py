class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = cost[0]
        b = cost[1]

        for i in range(2, len(cost)):
            temp = b
            b = cost[i] + min(a,b)
            a = temp
        
        return min(a,b)