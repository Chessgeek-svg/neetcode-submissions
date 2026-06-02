class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recursion(opens, closes, subset):
            if opens == closes == n:
                res.append(''.join(subset))
                return

            if opens < n:
                subset.append('(')
                recursion(opens+1, closes, subset)
                subset.pop()
            if opens > closes:
                subset.append(')')
                recursion(opens, closes+1, subset)
                subset.pop()
        
        recursion(0, 0, [])
        return res