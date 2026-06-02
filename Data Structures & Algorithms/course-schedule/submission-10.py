class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if not adj[i]:
                return True
            
            visited.add(i)
            for prereq in adj[i]:
                if not dfs(prereq):
                    return False
            visited.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True