class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        explored = []
        frontier = [(beginWord, 1)] # tuple(Word, distance from beginWord)
        unexplored = wordList

        heapq.heapify(frontier)

        while frontier:
            word, distance = heapq.heappop(frontier)
            if word in explored:
                continue
            if word == endWord:
                return distance
            adjacentNodes = self.adjacency(word, unexplored)
            for node in adjacentNodes:
                heapq.heappush(frontier, (node, distance + 1))
                unexplored.remove(node)
        
        return 0

        
    def adjacency(self, frontierWord, unexploredWords):
        adjacent = []
        for word in unexploredWords:
            different_chars = 0
            for i in range(len(word)):
                if word[i] != frontierWord[i]:
                    different_chars += 1
                if different_chars > 1:
                    break
            if 0 < different_chars <= 1:
                adjacent.append(word)
        return adjacent
