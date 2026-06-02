class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        result = []
        indexQueue = deque()

        for right in range(len(nums)):
            while indexQueue and nums[right] > nums[indexQueue[-1]]:
                indexQueue.pop()
            indexQueue.append(right)

            if left > indexQueue[0]:
                indexQueue.popleft()
            
            if right + 1 >= k:
                result.append(nums[indexQueue[0]])
                left += 1
            right += 1 
        return result