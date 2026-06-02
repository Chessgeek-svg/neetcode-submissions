class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [-1] * (len(temperatures))
        for i in range(len(temperatures)):
            j = i+1 
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    result[i] = (j-i)
                    break
                j += 1

            if result[i] == -1:
                result[i] = 0
            
        result
        return result