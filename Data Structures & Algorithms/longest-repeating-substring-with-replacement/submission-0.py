class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencyMap = {}
        L, curLength, maxLength = 0, 0, 0
        mostCommonCharacterCount = 0
        for R in range(len(s)):
            frequencyMap[s[R]] = frequencyMap.get(s[R], 0) + 1
            mostCommonCharacterCount = max(mostCommonCharacterCount, frequencyMap[s[R]])
            curLength += 1
        
            if curLength - k > mostCommonCharacterCount:
                frequencyMap[s[L]] -= 1
                L += 1
                curLength -= 1

            maxLength = max(maxLength, curLength)
        return maxLength
            
            
            
            # if s[L] == s[R]:
            #     curLength += 1
            #     maxLength = max(maxLength, curLength)
            #     continue
            # else:
            #     while k > 0:
            #         for char in s[R:]:
            #             if char != s[L]:
            #                 k -= 1
            #                 curLength += 1
            #                 maxLength = max(maxLength, curLength)