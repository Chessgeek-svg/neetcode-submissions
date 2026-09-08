class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        output = []

        def recursion(array, i, total):
            if total == target:
                output.append(array.copy())
                return
            if total > target or i == len(candidates):
                return
            
            array.append(candidates[i])
            recursion(array, i+1, total + candidates[i])
            array.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            recursion(array, i+1, total)

        recursion([], 0, 0)
        return output
