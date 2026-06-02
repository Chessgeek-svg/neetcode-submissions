class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            char = ord(char) - ord("a")
            if curr.children[char] == None:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            char = ord(char) - ord("a")
            if not curr.children[char]:
                return False
            curr = curr.children[char]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            char = ord(char) - ord("a")
            if not curr.children[char]:
                return False
            curr = curr.children[char]
        return True

        
        