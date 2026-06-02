class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if j < i:
                    continue
                if i == j:
                    palindromes += 1
                    continue
                midpoint = i + j
                if midpoint % 2:
                    #Odd midpoint = even # of chars
                    midpoint_left, midpoint_right = midpoint // 2, midpoint // 2 + 1
                    if s[i:midpoint_left+1] == s[midpoint_right:j+1][::-1]:
                        palindromes += 1
                else:
                    #even midpoint = odd # of chars
                    midpoint = midpoint // 2
                    if s[i:midpoint] == s[midpoint+1:j+1][::-1]:
                        palindromes += 1
        return palindromes