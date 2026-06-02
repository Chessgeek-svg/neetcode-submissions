class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        numberToIndex = {num : i for i, num in enumerate(nums1)}
        stack = []
        for element in nums2:
            while stack and stack[-1] < element:
                val = stack.pop()
                index = numberToIndex[val]
                res[index] = element
            if element in numberToIndex:
                stack.append(element)
        return res