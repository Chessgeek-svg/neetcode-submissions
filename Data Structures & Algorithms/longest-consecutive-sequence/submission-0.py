class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        foo = set(nums)
        bar = foo.copy()
        count = 0
        maxCount = 0
        for element in foo:
            while element -1 in bar:
                element -= 1
            while element in bar:
                bar.remove(element)
                element += 1
                count += 1
                maxCount = max(count, maxCount)
            count = 0

        return maxCount