class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.prefix_index = float('inf')

    def add(self, word: str) -> None:
        curr = self.root
        for i, c in enumerate(word):
            if c not in curr.children:
                curr.children[c] = TrieNode()
            if len(curr.children) > 1:
                self.prefix_index = min(self.prefix_index, i)
            curr = curr.children[c]
        self.prefix_index = min(self.prefix_index, len(word))
         
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for word in strs:
            trie.add(word)

        if not trie.prefix_index:
            return ''
        else:
            return strs[0][:trie.prefix_index]
