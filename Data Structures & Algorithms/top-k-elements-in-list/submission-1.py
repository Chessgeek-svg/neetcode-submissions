class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        values = [-val for val in counts.values()]
        list_counts = list(zip(values, counts.keys()))
        heapq.heapify(list_counts)
        res = [0] * k
        print(list_counts)
        for i in range(k):
            _, key = heapq.heappop(list_counts)
            res[i] = key
        return res