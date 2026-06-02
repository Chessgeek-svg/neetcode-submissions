class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openClose = { ")" : "(", "]" : "[", "}" : "{" }
        for char in s:
            if char in openClose:
                if stack and stack[-1] == openClose[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0