class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = 1
        # zeroInArray = None
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         product = product * nums[i]
        #     elif zeroInArray is None:
        #         zeroInArray = i
        #     else:
        #         return [0] * len(nums)
    
        
        # if zeroInArray:
        #     output = [0] * len(nums)
        #     output[zeroInArray] = product
        # else:
        #     output = []
        #     for i in range(len(nums)):
        #         output.append(int(product / nums[i]))
        # return output

        # prefixProduct = [nums[0]]
        # postfixProduct = [nums[-1]]
        # for i in range(1, len(nums)):
        #     prefixProduct.append(prefixProduct[i-1] * nums[i])
        #     postfixProduct.append(postfixProduct[i-1] * nums[-i-1])
        #     print(postfixProduct, nums[-i-1])

        # output = [postfixProduct[-2]]
        # postfixProduct = postfixProduct[::-1]
        # for i in range(1, len(nums)-1):
        #     output.append(prefixProduct[i-1] * postfixProduct[i+1])
        # output.append(prefixProduct[-2])
        # print(prefixProduct, postfixProduct)

        # return output
            
        output = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output