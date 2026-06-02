class Graph:
    
    def __init__(self):
        self.adjacencyList = {}


    def addEdge(self, src: int, dst: int) -> None:
        if not src in self.adjacencyList:
            self.adjacencyList[src] = set()
        if not dst in self.adjacencyList:
            self.adjacencyList[dst] = set()
        
        self.adjacencyList[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if not src in self.adjacencyList or not dst in self.adjacencyList[src]:
            return False
        self.adjacencyList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)

    def dfs(self, src: int, dst: int, visited):
        if src == dst:
            return True

        visited.add(src)
        for node in self.adjacencyList[src]:
            if node not in visited:
                if self.dfs(node, dst, visited):
                    return True
        return False


