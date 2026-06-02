class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for crs, neighbor in prerequisites:
            adj[crs].append(neighbor)

        topSort = []
        path = []
        visit = set()

        def dfs(course, path, visit, topSort):
            if course in path:
                return False
            if course in visit:
                return True
            visit.add(course)
            path.append(course)

            for neighbor in adj[course]:
                if not dfs(neighbor, path, visit, topSort):
                    return False
            topSort.append(course)
            path.pop()
            return True

        for i in range(numCourses):
            if not dfs(i, path, visit, topSort):
                return False
            
        return set(topSort) == visit