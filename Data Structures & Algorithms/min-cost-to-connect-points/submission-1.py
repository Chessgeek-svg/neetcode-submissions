class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        LEN_POINTS = len(points)

        def calculateDistances(start):
            res = []
            for point in points:
                if tuple(point) in visited or point == start:
                    continue
                distance = abs(point[0] - start[0]) + abs(point[1] - start[1])
                heapq.heappush(res, (distance, point))
            return res

        visited = set()
        visited.add(tuple(points[0]))
        frontier = calculateDistances(points[0])
        pathCost = 0
        while len(visited) < LEN_POINTS:
            weight, point = heapq.heappop(frontier)
            if tuple(point) in visited:
                continue
            pathCost += weight
            visited.add(tuple(point))
            newEdges = calculateDistances(point)
            for edge in newEdges:
                heapq.heappush(frontier, edge)
            # print(pathCost)
            # print(frontier)
            # print(visited)

        return pathCost
    