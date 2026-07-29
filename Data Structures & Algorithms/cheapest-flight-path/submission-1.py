class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for from_i, to_i, price_i in flights:
            adj[from_i].append([to_i, price_i])
        explored = {}
        frontier = [(0, -1, src)] #cost, stops, source
        heapq.heapify(frontier)
        while frontier:
            cost, stops, source = heapq.heappop(frontier)
            if stops > k or (source in explored and explored[source] <= stops):
                continue
            if source == dst:
                return cost
            explored[source] = stops
            for to_i, price_i in adj[source]:
                heapq.heappush(frontier, (cost + price_i, stops + 1, to_i))
        return -1