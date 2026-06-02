class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            charCounts = [0] * 26
            for char in string:
                charCounts[ord(char) - ord('a')] += 1
            if tuple(charCounts) not in anagrams:
                anagrams[(tuple(charCounts))] = [string]
            else:
                anagrams[(tuple(charCounts))].append(string)
        return list(anagrams.values())