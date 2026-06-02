class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        minSpeed = right
        while left <= right:
            midpoint = (right - left) // 2 + left
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / midpoint)
            if hours <= h:
                minSpeed = midpoint
                right = midpoint - 1
            else:
                left = midpoint + 1

        return minSpeed
        