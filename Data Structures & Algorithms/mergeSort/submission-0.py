# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)
        
    def mergeSortHelper(self, pairs:List[Pair], start:int, end:int) -> List[Pair]:
        if end - start <= 0:
            return pairs
        
        midpoint = (end + start) // 2

        self.mergeSortHelper(pairs, start, midpoint)
        self.mergeSortHelper(pairs, midpoint+1, end)
        self.merge(pairs, start, midpoint, end)

        return(pairs)

    def merge(self, arr:List[Pair], start:int, midpoint:int, end:int) -> None:
        left = arr[start: midpoint+1]
        right = arr[midpoint+1: end+1]
        i, j, k = 0, 0, start

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1


    





