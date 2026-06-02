class Solution:
    def isValid(self, s: str) -> bool:
        lastOpened = 0
        opensMinusCloses = 0
        for char in s:
            if char == "[" or char == "{" or char == "(":
                lastOpened = s.index(char)
                opensMinusCloses += 1
                continue
            elif char == "]":
                if s[lastOpened] != "[":
                    return False
            elif char == "}":
                if s[lastOpened] != "{":
                    return False
            else:
                 if s[lastOpened] != "(":
                    return False
            opensMinusCloses -= 1
            if opensMinusCloses < 0:
                return False
            lastOpened -= 1
        if opensMinusCloses != 0:
            return False
        return True
