class Solution:
    def trap(self, height: List[int]) -> int:
        prefixSum = []
        curMax = 0
        for i in range(len(height)):
            curMax = max(curMax, height[i])
            prefixSum.append(curMax)
        
        suffixSum = [0] * len(height)
        curMax = 0
        for i in range(len(height)-1, -1, -1):
            curMax = max(curMax, height[i])
            suffixSum[i] = curMax
        
        water = 0
        for i in range(len(height)):
            water += (min(prefixSum[i], suffixSum[i]) - height[i])
        return water