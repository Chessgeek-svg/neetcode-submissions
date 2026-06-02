class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, char in enumerate(s):
            lastIndex[char] = i
        size = 0
        res = []
        end = 0
        for i in range(len(s)):
            size += 1
            end = max(end, lastIndex[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res