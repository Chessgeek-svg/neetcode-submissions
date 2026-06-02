class Solution:
    def isValid(self, s: str) -> bool:

        lastOpened = []

        for char in s:

            if char == "[" or char == "{" or char == "(":
                lastOpened.append(char)
                continue

            elif not lastOpened:
                return False

            elif char == "]":
                if lastOpened[-1] != "[":
                    return False

            elif char == "}":
                if lastOpened[-1] != "{":
                    return False

            else:
                if lastOpened[-1] != "(":
                    return False

            lastOpened.pop()

        if len(lastOpened) != 0:
            return False
            
        return True