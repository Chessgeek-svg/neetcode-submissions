class MedianFinder:

    def __init__(self):
        self.minHalf, self.maxHalf = [], []
        heapq.heapify(self.minHalf)
        heapq.heapify(self.maxHalf)

    def addNum(self, num: int) -> None:
        mid = float("-inf")
        if self.minHalf:
            mid = -self.minHalf[0]
        if num > mid:
            heapq.heappush(self.maxHalf, num)
        else:
            heapq.heappush(self.minHalf, -num)
        if len(self.minHalf) > len(self.maxHalf) + 1:
            self.BalanceHeaps(self.minHalf, self.maxHalf)
        elif len(self.maxHalf) > len(self.minHalf) + 1:
            self.BalanceHeaps(self.maxHalf, self.minHalf)

    def findMedian(self) -> float:
        if len(self.minHalf) > len(self.maxHalf):
            return -self.minHalf[0]
        elif len(self.minHalf) < len(self.maxHalf):
            return self.maxHalf[0]
        else:
            return (self.maxHalf[0] - self.minHalf[0]) / 2

    def BalanceHeaps(self, bigHalf, smallHalf) -> None:
        val = heapq.heappop(bigHalf)
        heapq.heappush(smallHalf, -val)
    