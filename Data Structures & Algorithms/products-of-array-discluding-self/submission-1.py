class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroInArray = None
        for i in range(len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            elif zeroInArray is None:
                zeroInArray = i
            else:
                return [0] * len(nums)
    
        
        if zeroInArray:
            output = [0] * len(nums)
            output[zeroInArray] = product
        else:
            output = []
            for i in range(len(nums)):
                output.append(int(product / nums[i]))
        return output
        