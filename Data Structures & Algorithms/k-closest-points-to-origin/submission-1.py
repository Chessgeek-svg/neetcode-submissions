class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            euclid = self.euclid(points[i])
            heap.append([euclid, points[i]])
        
        heapq.heapify(heap)

        res = []
        for i in range(k):
            dist, [x, y] = heapq.heappop(heap)
            res.append([x, y])
        
        return res
    
    def euclid(self, xy: List[int]):
        return (math.sqrt(xy[0]**2 + xy[1]**2))