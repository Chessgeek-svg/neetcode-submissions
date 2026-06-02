class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = Counter(s1)
        counts_s2 = Counter(s2[:len(s1)])
        if counts_s1 == counts_s2:
            return True
        for right in range(len(s1), len(s2)):
            counts_s2[s2[right]] += 1
            left = right - len(s1)
            counts_s2[s2[left]] -= 1
            if counts_s2[s2[left]] == 0:
                del counts_s2[s2[left]]
            if counts_s2 == counts_s1:
                return True
        return False