from typing import Dict, List


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node: TrieNode = self.root

        for i in range(len(word)):
            c: str = word[i]
            next_node = node.children.get(c, TrieNode(c))
            next_node.words.append(word)

            node.children[c] = next_node
            node = next_node

            if i == len(word) - 1:
                node.is_leaf = True


    def prefix_search(self, word: str) -> List[str]:
        node: TrieNode = self.root

        for c in word:
            if c in node.children.keys():
                node = node.children[c]
            else:
                return []
        return node.words

class TrieNode:
    def __init__(self, c: str = None):
        self.c = c
        self.children: Dict[str, TrieNode] = {}
        self.words = []


trie = Trie()
trie.add_word('chris')
trie.add_word('christian')
trie.add_word('christmas')
matches = trie.prefix_search('ch')
print(matches)