class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            par_a, par_b = find(a), find(b)
            if par_a == par_b:
                return False
            
            parent[par_a] = par_b
            
            return True

        for a,b in edges:
            if not union(a,b):
                return False
        return True