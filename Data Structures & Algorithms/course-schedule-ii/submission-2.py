class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        def schedule(i):
            if i in visited:
                return False
            
            visited.add(i)
            for prereq in adj[i]:
                if not schedule(prereq):
                    return False
            visited.remove(i)
            adj[i] = []
            if i not in res:
                res.append(i)
            return True
        
        res = []
        for i in range(numCourses):
            if not schedule(i):
                return []
        return res
            
                