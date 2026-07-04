class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            dist = self.euclid(point[0], point[1])
            distances.append((dist, point)) # (float, [int, int])
        heapq.heapify(distances)

        output = []
        for i in range(k):
            _, point = heapq.heappop(distances)
            output.append(point)
        return output

    def euclid(self, a, b) -> float:
        return math.sqrt((a**2) + (b**2))