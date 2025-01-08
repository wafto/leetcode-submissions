class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str) -> int:
        cur = self.root
        for c1, c2 in zip(word, reversed(word)):
            pair = (c1, c2)
            if pair not in cur.children:
                cur.children[pair] = TrieNode()
            cur = cur.children[pair]
            cur.count += 1
        return cur.count - 1
        
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        output = 0

        for word in reversed(words):
            output += trie.add(word)

        return output