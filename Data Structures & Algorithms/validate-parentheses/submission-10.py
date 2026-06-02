class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {
            ")" : "(", 
            "}" : "{", 
            "]" : "["
        }
        stack = []
        for char in s:
            if char in charMap:
                if not stack or stack[-1] != charMap[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return True if not stack else False