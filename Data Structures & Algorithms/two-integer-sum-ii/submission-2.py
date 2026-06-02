class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1 2 3 5 8 13 21
        L, R = 0, 1
        while numbers[L] + numbers[R] != target:
            while numbers[L] + numbers[R] < target:
                L += 1
                R += 1
            while numbers[L] + numbers[R] > target:
                L -= 1
        return [L+1, R+1]
