class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        def find(n):
            if par[n] != n:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            par[p1] = p2
            return True
        
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            if not union(n1, n2):
                return edge


