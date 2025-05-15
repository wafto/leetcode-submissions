class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        ord_a = ord('a')

        if len(words) <= 1:
            return True

        for i, c in enumerate(order):
            hashmap[c] = chr(ord_a + i)

        def humanize(word: str) -> str:
            w = list(word)
            for i in range(len(w)):
                w[i] = hashmap[w[i]]
            return ''.join(w)

        for i in range(len(words)):
            words[i] = humanize(words[i])

        for i in range(1, len(words)):
            if words[i - 1] > words[i]:
                return False

        return True
            
        

