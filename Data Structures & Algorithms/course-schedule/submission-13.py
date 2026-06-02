class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        def validPrereqs(i):
            if i in visited:
                return False
            if adj[i] == []:
                return True
            
            visited.add(i)
            for prereq in adj[i]:
                if not validPrereqs(prereq):
                    return False
            visited.remove(i)
            adj[i] = []
            return True


        for i in range(numCourses):
            if not validPrereqs(i):
                return False
        return True