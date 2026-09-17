class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            par_a, par_b = find(a), find(b)
            if par_a == par_b:
                return False
            if rank[par_a] < rank[par_b]:
                parent[par_a] = par_b
            elif rank[par_b] < rank[par_a]:
                parent[par_b] = par_a
            else:
                parent[par_a] = par_b
                rank[par_b] += 1
            return True

        for a, b in edges:
            if not union(a, b):
                return False
        return True
