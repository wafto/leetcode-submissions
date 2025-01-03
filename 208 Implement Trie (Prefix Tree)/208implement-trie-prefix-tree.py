class TrieNode:
    def __init__(self):
        self.mapping = {}
        self.word = False

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.mapping:
                curr.mapping[c] = TrieNode()
            curr = curr.mapping[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c not in curr.mapping:
                return False
            curr = curr.mapping[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c not in curr.mapping:
                return False
            curr = curr.mapping[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)