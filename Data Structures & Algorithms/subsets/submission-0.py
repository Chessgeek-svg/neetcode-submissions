class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        length = len(nums)

        subset = []
        def subsetHelper(nums: List[int], start: int):
            if start >= length:
                res.append(subset.copy())
                return

            subset.append(nums[start])
            
            subsetHelper(nums, start+1)
            subset.pop()
            subsetHelper(nums, start+1)


        subsetHelper(nums, 0)
        return res
        

        
        
            
        