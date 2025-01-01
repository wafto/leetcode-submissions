class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.lower().replace(',', ' ').replace('.', ' ').split()

        def onlychars(w: str) -> str:
            o = ''
            for c in w:
                v = ord(c)
                if v >= 97 and v <= 122:
                    o += c
            return o

        words = list(map(onlychars, words))
        mapping = dict()

        for word in words:
            if word not in banned:
                mapping[word] = 1 + mapping.get(word, 0)

        occur = ''
        times = -1

        for word, score in mapping.items():
            if score > times:
                occur = word
                times = score

        return occur