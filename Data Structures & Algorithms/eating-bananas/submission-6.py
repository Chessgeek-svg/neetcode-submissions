class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while (left <= right):
            eatingTime = 0
            midpoint = (left+right) // 2
            for i in piles:
                eatingTime += -(i // -midpoint)
            if eatingTime > h:
                left = midpoint + 1
            else:
                result = midpoint
                right = midpoint -1
        
        return result