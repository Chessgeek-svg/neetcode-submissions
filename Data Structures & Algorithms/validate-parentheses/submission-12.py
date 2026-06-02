class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openClose = {'(' : ')', '{' : '}', '[' : ']'}
        for char in s:
            if char in openClose.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if char != openClose[prev]:
                    return False
        return len(stack) == 0