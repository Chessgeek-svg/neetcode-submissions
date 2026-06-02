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

        def printCombinations(i, subset):
            if i == len(digits):
                res.append(subset)
                return
            
            for char in numberToLetter[digits[i]]:
                printCombinations(i+1, subset + char)
        if digits:
            printCombinations(0, "")
        return res