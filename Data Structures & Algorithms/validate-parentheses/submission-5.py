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
                if stack:
                    if stack[-1] != charMap[char]:
                        return False
                else:
                    return False
                stack.pop(-1)
            else:
                stack.append(char)
        if stack:
            return False
        return True