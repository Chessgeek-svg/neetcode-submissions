class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, neighbor in prerequisites:
            adj[course].append(neighbor)

        def dfs(src, visit, path, topSort):
            if src in path:
                return False
            elif src in visit:
                return True
            visit.add(src)
            path.append(src)

            for neighbor in adj[src]:
                if not dfs(neighbor, visit, path, topSort):
                    return False
            topSort.append(src)
            path.pop()
            return True

        visit = set()
        path = []
        topSort = []
        for i in range(numCourses):
            if not dfs(i, visit, path, topSort):
                return False
        return True if set(topSort) == visit else False