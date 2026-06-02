class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = Counter(s1)
        counts_s2 = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            if s2[right] not in counts_s1:
                counts_s2 = defaultdict(int)
                left = right + 1
                continue
            counts_s2[s2[right]] += 1
            while counts_s2[s2[right]] > counts_s1[s2[right]]:
                counts_s2[s2[left]] -= 1
                left += 1
            if counts_s2 == counts_s1:
                return True
        return False