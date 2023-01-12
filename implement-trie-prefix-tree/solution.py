class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        word = list(reversed(word))
        node = self.root
        while len(word) > 0:
            letter = word.pop()
            if letter not in node.children:
               node.children[letter] = Node()
            node = node.children[letter]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        word = list(reversed(word))
        node = self.root
        while len(word) > 0:
            letter = word.pop()
            if letter not in node.children:
               return False
            node = node.children[letter]
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        word = list(reversed(prefix))
        node = self.root
        while len(word) > 0:
            letter = word.pop()
            if letter not in node.children:
               return False
            node = node.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)