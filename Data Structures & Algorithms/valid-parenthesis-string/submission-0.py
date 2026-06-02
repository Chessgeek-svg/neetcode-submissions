class Solution:
    def checkValidString(self, s: str) -> bool:
        maxOpens = minOpens = closes = 0
        for i in range(len(s)):
            if s[i] == '(':
                minOpens += 1
                maxOpens += 1
            elif s[i] == ')':
                minOpens -= 1
                maxOpens -= 1
            else:
                maxOpens += 1
                minOpens -= 1
            if maxOpens < 0:
                return False
            if minOpens < 0:
                minOpens = 0
            
        return closes >= minOpens