class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = []
        num1Index = {num : i for i, num in enumerate(nums1)}
        for element in nums2:
            while stack and element > stack[-1]:
                num = stack.pop()
                index = num1Index[num]
                res[index] = element
            if element in nums1:
                stack.append(element)
        return res