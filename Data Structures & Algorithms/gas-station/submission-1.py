class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        resultIndex = 0
        currentGas = 0
        for i in range(len(gas)):
            currentGas += gas[i]
            currentGas -= cost[i]
            if currentGas < 0:
                resultIndex = i+1
                currentGas = 0
        return resultIndex
        