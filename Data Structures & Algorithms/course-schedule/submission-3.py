# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {i: [] for i in range(numCourses)}
        for val, edge in prerequisites:
            nodes[val].append(edge)

        visited = set()
        
        def dfs(key):
            if key in visited:
                return False
            if nodes[key] == []:
                return True

            visited.add(key)
            
            edges = nodes[key]
            for edge in edges:
                if not dfs(edge):
                    return False
            
            visited.remove(key)
            nodes[key] = []
            return True


        for key in nodes.keys():
            if not dfs(key):
                return False
        return True
            

            





        