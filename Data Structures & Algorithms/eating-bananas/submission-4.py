class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        divisor = (h // len(piles))
        low = 1
        high = (max(i for i in piles) + divisor + 1) // divisor

        while low <= high:
            mid = (low + high) // 2
            eatingSpeed = self.eatingSpeedCheck(piles[:], mid, h)
            if eatingSpeed < 0:
                low = mid + 1
            else:
                high = mid -1 

        return low


    def eatingSpeedCheck(self, arr: List[int], mid:int, h:int) -> int:
        for i in range(len(arr)):
            while arr[i] > 0 and h > 0:
                temp = (arr[i] + mid -1) // mid
                arr[i] -= temp*mid
                h -= temp

        if arr[-1] > 0 or h < 0:
            return -1
        else:
            return 1





