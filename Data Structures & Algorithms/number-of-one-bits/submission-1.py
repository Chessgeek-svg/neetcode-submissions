class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if 1 & n:
                count += 1
            n = n >> 1
        return count




# AND
n = 1 & 1

# OR
n = 1 | 0

# XOR
n = 0 ^ 1

# NOT (negation)
n = ~n

# Bit shifting
n = 1
n = n << 1
n = n >> 1
