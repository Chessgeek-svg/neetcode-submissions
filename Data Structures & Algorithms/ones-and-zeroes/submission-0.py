class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = {}
        for string in strs:
            zeros, ones = 0, 0
            for char in string:
                if char == "0":
                    zeros += 1
                elif char == "1":
                    ones += 1
            counts[string] = [zeros,ones]
        knapsack = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for string in strs:
            zeros, ones = counts[string]
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    knapsack[i][j] = max(knapsack[i][j], knapsack[i-zeros][j-ones] + 1)
        return knapsack[m][n]
