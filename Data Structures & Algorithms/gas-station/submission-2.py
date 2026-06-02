class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        surplus = index = 0
        for i in range(len(gas)):
            surplus += gas[i]
            surplus -= cost[i]
            if surplus < 0:
                index = i + 1
                surplus = 0
        return index
        