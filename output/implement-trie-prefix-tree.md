# Implement Trie (Prefix Tree)

## Link

https://leetcode.com/problems/implement-trie-prefix-tree/

## Where

Leetcode

## Difficulty

Medium

## Description

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

## Solution Main Idea

Make trie lol


## Code

```python
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
```
