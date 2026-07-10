class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            distances.append([dist, point])
        heapq.heapify(distances)
        result = []
        for i in range(k):
            result.append(heapq.heappop(distances)[1])
        return result