class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberToLetter = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res = []

        def dfs(i, substring):
            if len(substring) == len(digits):
                res.append("".join(substring.copy()))
                print(res)
                return
            
            for char in numberToLetter[digits[i]]:
                substring.append(char)
                dfs(i+1, substring)
                substring.pop()
        
        if digits : dfs(0, [])

        return res