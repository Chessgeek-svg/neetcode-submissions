class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1][1]:
                index, val = stack.pop()
                res[index] = nums2[i]
            if nums2[i] in nums1:
                stack.append((nums1.index(nums2[i]), nums2[i]))
        return res
