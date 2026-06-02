class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minSpeed = right
        while left <= right:
            midpoint = (left + right) // 2
            if self.sufficientSpeed(midpoint, piles, h):
                minSpeed = midpoint
                right = midpoint - 1
            else:
                left = midpoint + 1
        return minSpeed
    

    def sufficientSpeed(self, midpoint, piles, h):
        result = 0
        for pile in piles:
            if pile % midpoint == 0:
                result += pile / midpoint
            else:
                result += pile // midpoint + 1
        return result <= h