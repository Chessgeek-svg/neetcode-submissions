class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Index = {num : index for index, num in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                index = nums1Index[val]
                res[index] = nums2[i]
            if nums2[i] in nums1:
                stack.append(nums2[i])
        return res