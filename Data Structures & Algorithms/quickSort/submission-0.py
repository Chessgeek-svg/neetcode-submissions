# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs)-1)
        
    def quickSortHelper(self, pairs: List[Pair], start:int, end:int):
        if end - start <= 0:
            return pairs
        
        pivot = pairs[end]
        left = start

        for i in range(start, end):
            if pairs[i].key < pivot.key:
                temp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = temp
                left += 1
        
        pairs[end] = pairs[left]
        pairs[left] = pivot

        self.quickSortHelper(pairs, start, left-1)
        self.quickSortHelper(pairs, left+1, end)

        return pairs
        