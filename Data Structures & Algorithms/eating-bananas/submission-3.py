class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if h = len(piles):
        #   k = max(piles[i])
        #h / len(piles) == divisor
        #   k = max(piles[i]) / divisor
        #for i in piles:
        #   k += piles[i] / (divisor)
        #binary search:
        divisor = (h // len(piles))
        low = 1
        high = (max(i for i in piles) + divisor + 1) // divisor
        #print(low, high, divisor)
        #counter = 0
        #return 2
        while low <= high:
            mid = (low + high) // 2
            #print(low, high, mid)

            eatingSpeed = self.eatingSpeedCheck(piles[:], mid, h)
            if eatingSpeed < 0:
                low = mid + 1
            else:
                high = mid -1 
            #counter += 1

        return low


    def eatingSpeedCheck(self, arr: List[int], mid:int, h:int) -> int:
        for i in range(len(arr)):
            while arr[i] > 0 and h > 0:
                temp = (arr[i] + mid -1) // mid
                #print("temp:", temp, "mid:", mid, "arr[i]:", arr[i], "h:", h)
                arr[i] -= temp*mid
                h -= temp

        if arr[-1] > 0 or h < 0:
            return -1
        else:
            return 1





