class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        for string in strs:
            temp = "".join(sorted(string))
            wordDict[temp] = wordDict.get(temp, [])
            wordDict[temp].append(string)
        res = [value for value in wordDict.values()]
        return res