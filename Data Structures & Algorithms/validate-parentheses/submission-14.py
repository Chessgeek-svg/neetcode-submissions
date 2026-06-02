class Solution:
    def isValid(self, s: str) -> bool:
        pairings = { '}' : '{', ']' : '[', ')' : '('}

        stack = []
        for char in s:
            if char in pairings:
                if stack and stack[-1] == pairings[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False