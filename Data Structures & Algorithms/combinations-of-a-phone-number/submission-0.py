class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(digitsIndex, subset):
            if len(subset) == len(digits):
                res.append("".join(subset[:]))
                return
            
            
            for i in range(4):
                if i == 3 and digits[digitsIndex] not in "79":
                    break
                char = digitToChar[digits[digitsIndex]][i]

                subset.append(char)
                dfs(digitsIndex + 1, subset)
                subset.pop()
        
        dfs(0, [])
        return res
