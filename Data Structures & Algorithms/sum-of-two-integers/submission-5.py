class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            change = (a&b) << 1
            a = a^b
            b = change
        return a if b == 0 else a & mask