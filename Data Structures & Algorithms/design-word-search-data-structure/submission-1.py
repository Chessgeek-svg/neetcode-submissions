class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str, curr = None) -> bool:
        if curr == None:
            curr = self.root
        for char in word:
            if char not in curr.children:
                if char == ".":
                    index = word.index(char) + 1
                    for key in curr.children:
                        if self.search(word[index:], curr.children[key]):
                            return True
                return False
            curr = curr.children[char]
        return curr.word
