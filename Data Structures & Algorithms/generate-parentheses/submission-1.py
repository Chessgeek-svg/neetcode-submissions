class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recursion(start, end, s):
            if start == end == n:
                res.append(s)
                return
            
            if start < n:
                recursion(start + 1, end, s + "(")

            if end < start:
                recursion(start, end + 1, s + ")")
        
        recursion(0, 0, "")
        return list(set(res))