class Solution:
    def canCompleteCircuit(self, gas, cost):
        surplus = 0
        index = 0
        total = 0
        for i in range(len(gas)):
            net = gas[i] - cost[i]
            surplus += net
            total += net
            if surplus < 0:
                index = i + 1
                surplus = 0
        return index if total >= 0 else -1