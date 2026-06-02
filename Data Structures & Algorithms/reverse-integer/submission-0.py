class Solution:
    def reverse(self, x: int) -> int:
        original = str(abs(x))
        rev = 0
        for char in original[::-1]:
            rev = rev * 10 + int(char)
        if x < 0:
            rev *= -1
        if -(1<<31) > rev or (1<<31) - 1 < rev:
            return 0
        return rev