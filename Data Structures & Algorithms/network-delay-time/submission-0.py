class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = [-1] * (n + 1)
        adj = {}
        for num in range(1, n+1):
            adj[num] = []
        for source, dest, cost in times:
            adj[source].append((cost, dest))
        
        shortest = {}
        minHeap = [(0, k)]
        while minHeap:
            cost, dest = heapq.heappop(minHeap)
            if dest in shortest and shortest[dest] <= cost:
                continue
            shortest[dest] = cost
            res[dest] = cost

            for adjCost, nextDest in adj[dest]:
                if nextDest in shortest and shortest[nextDest] <= cost + adjCost:
                    continue
                else:
                    minHeap.append((cost + adjCost, nextDest))

        return max(res[1:]) if min(res[1:]) > -1 else -1