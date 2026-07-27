class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for ticket in sorted(tickets, reverse=True):
            departure, destination = ticket[0], ticket[1]
            adj[departure].append(destination)

        res = []
        def dfs(departure):
            while adj[departure]:
                dfs(adj[departure].pop())
            res.append(departure)
        
        dfs("JFK")

        return res[::-1]
