class TrieNode:
    def __init__(self):
        self.children = {}
        self.indexes = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.words = []
    
    def add(self, word: str) -> None:
        self.words.append(word)
        index = len(self.words) - 1
        curr = self.root
        curr.indexes.append(index)
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            if len(curr.indexes) < 3:
                curr.indexes.append(index)

    def suggest(self, prefix: str) -> List[str]:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return []
            curr = curr.children[c]
        suggestions = []
        for i in curr.indexes:
            suggestions.append(self.words[i])
        return suggestions
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prefixTree = Trie()

        for product in sorted(products):
            prefixTree.add(product)

        answer = []

        for i in range(len(searchWord)):
            answer.append(prefixTree.suggest(searchWord[:i + 1]))

        return answer