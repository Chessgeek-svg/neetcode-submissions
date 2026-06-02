class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        sublistList = []
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in wordDict.keys():
                wordDict[sortedWord] = [word]
            else:
                wordDict[sortedWord].append(word)
        for value in wordDict.values():
            sublistList.append(value)
        return sublistList
            
        