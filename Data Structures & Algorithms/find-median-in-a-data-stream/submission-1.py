class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums = sorted(self.nums)
        length = len(self.nums)
        median = (length - 1) // 2
        if length % 2:
            return float(self.nums[median])
        else:
            return (self.nums[median] + self.nums[median + 1]) / 2
        