class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            buckets = [0] * 26
            for char in word:
                buckets[ord(char) - ord('a')] += 1
            res[tuple(buckets)].append(word)
        return list(res.values())