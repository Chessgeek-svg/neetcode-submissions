class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        numqueue = deque()
        result = []

        for right in range(len(nums)):
            while numqueue and nums[right] > nums[numqueue[-1]]:
                numqueue.pop()
            
            numqueue.append(right)

            if left > numqueue[0]:
                numqueue.popleft()

            if right + 1 >= k:
                result.append(nums[numqueue[0]])
                left += 1
            
            right += 1

        return result