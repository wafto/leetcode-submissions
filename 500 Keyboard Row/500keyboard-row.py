class Solution:
    def __init__(self):
        self.mp = {
            'q': 1,
            'w': 1,
            'e': 1,
            'r': 1,
            't': 1,
            'y': 1,
            'u': 1,
            'i': 1,
            'o': 1,
            'p': 1,
            'a': 2,
            's': 2,
            'd': 2,
            'f': 2,
            'g': 2,
            'h': 2,
            'j': 2,
            'k': 2,
            'l': 2,
            'z': 3,
            'x': 3,
            'c': 3,
            'v': 3,
            'b': 3,
            'n': 3,
            'm': 3,
        }
    
    def wordGroup(self, w: str) -> bool:
        if len(w) == 0:
            return False

        w = w.lower()
        g = self.mp[w[0]]

        for c in w:
            if g != self.mp[c]:
                return False
            g = self.mp[c]

        return True


    def findWords(self, words: List[str]) -> List[str]:
        output = []

        for word in words:
            if self.wordGroup(word):
                output.append(word)

        return output
