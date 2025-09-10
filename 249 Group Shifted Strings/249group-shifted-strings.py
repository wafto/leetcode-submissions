class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        def hashword(word: str) -> str:
            key = []
            for a, b in zip(word, word[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return ''.join(key)

        for word in strings:
            hashmap[hashword(word)].append(word)

        return list(hashmap.values())

        