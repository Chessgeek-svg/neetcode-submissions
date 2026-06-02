class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recursion(start, end, substring):
            if start == end == n:
                res.append(substring)
                return
            
            if start < n:
                recursion(start + 1, end, substring + '(')
            
            if end < start:
                recursion(start, end + 1, substring + ')')
                
        recursion(0, 0, '')
        return res