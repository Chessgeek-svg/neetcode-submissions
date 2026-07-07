class MedianFinder:

    def __init__(self):
        self.lowerhalf, self.upperhalf = [], []
        heapq.heapify(self.lowerhalf)
        heapq.heapify(self.upperhalf)
        self.upperlength, self.lowerlength = 0, 0

    def addNum(self, num: int) -> None:
        if self.lowerhalf:
            med = -self.lowerhalf[0]
        else:
            med = float("-inf")
        if num > med:
            heapq.heappush(self.upperhalf, num)
            self.upperlength += 1
        else:
            heapq.heappush(self.lowerhalf, -num)
            self.lowerlength += 1
        if self.upperlength > self.lowerlength + 1:
            val = heapq.heappop(self.upperhalf)
            heapq.heappush(self.lowerhalf, -val)
            self.upperlength -= 1
            self.lowerlength += 1
        elif self.lowerlength > self.upperlength + 1:
            val = heapq.heappop(self.lowerhalf)
            heapq.heappush(self.upperhalf, -val)
            self.upperlength += 1
            self.lowerlength -= 1

    def findMedian(self) -> float:
        if self.upperlength > self.lowerlength:
            return self.upperhalf[0]
        elif self.lowerlength > self.upperlength:
            return -self.lowerhalf[0]
        else:
            return (-self.lowerhalf[0] + self.upperhalf[0]) / 2
        