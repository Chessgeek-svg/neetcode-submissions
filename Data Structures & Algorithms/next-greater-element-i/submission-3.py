class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numToIndex = {num: index for index, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1][1]:
                stackIndex, stackVal = stack.pop()
                num1Index = numToIndex[stackVal]
                res[num1Index] = nums2[i]
            if nums2[i] in nums1:
                stack.append((i, nums2[i]))
        return res