class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        usable = [False] * len(triplets)
        for i in range(len(triplets)):
            triplet = triplets[i]
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            usable[i] = True
        res = [0, 0, 0]
        for i in range(len(triplets)):
            triplet = triplets[i]
            if usable[i]:
                res = [max(res[0], triplet[0]), max(res[1], triplet[1]), max(res[2], triplet[2])]
        return res == target