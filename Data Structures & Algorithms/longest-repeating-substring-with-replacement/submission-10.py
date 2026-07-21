class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = {}
        maxFreq, maxLen, left = 0, 0, 0
        for i in range(len(s)):
            freqDict[s[i]] = freqDict.get(s[i], 0) + 1
            maxFreq = max(maxFreq, freqDict[s[i]])
            if i - left + 1 > k + maxFreq:
                freqDict[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, i - left + 1)
        return maxLen