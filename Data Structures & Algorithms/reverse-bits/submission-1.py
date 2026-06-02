class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for i in range(31):
            if n&1 == 1:
                m += 1
            n = n >> 1
            m = m << 1
        
        return m if n&1 == 0 else m+1