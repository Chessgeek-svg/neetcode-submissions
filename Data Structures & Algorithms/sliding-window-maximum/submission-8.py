class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        queue = deque()
        res = []

        for right in range(len(nums)):
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            queue.append(right)

            if left > queue[0]:
                queue.popleft()

            if right >= k - 1:
                res.append(nums[queue[0]])
                left += 1
            
        return res