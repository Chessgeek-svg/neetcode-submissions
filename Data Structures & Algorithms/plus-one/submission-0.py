class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        index = 0
        while index < len(digits) and digits[index] == 9:
            digits[index] = 0
            index += 1
        if index == len(digits):
            digits.append(1)
        else:
            digits[index] += 1
        return digits[::-1]
