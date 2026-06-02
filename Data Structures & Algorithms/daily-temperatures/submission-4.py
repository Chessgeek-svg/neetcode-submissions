class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((i, temperatures[i]))
        
        return result