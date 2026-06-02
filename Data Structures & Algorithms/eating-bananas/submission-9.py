class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minSpeed = right

        while left <= right:
            midpoint = (left + right) // 2
            currentHours = 0
            for pile in piles:
                currentHours += math.ceil(float(pile)/midpoint)
            if currentHours <= h:
                minSpeed = midpoint
                right = midpoint - 1
            else:
                left = midpoint + 1
        
        return minSpeed