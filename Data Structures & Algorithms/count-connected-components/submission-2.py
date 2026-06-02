class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        numComponents = n
        par = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            return True

        for n1, n2 in edges:
            if union(n1, n2):
                numComponents -= 1
        return numComponents