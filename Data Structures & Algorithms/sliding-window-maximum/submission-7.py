class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        numQueue = deque()

        for right in range(len(nums)):
            while numQueue and nums[numQueue[-1]] < nums[right]:
                numQueue.pop()
            
            numQueue.append(right)

            if left > numQueue[0]:
                numQueue.popleft()

            if right + 1 >= k:
                res.append(nums[numQueue[0]])
                left += 1
            
        return res