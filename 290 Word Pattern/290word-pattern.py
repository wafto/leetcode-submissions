class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        reverse = {}

        for char, word in zip(list(pattern), words):
            if char not in mapping and word not in reverse:
                mapping[char] = word
                reverse[word] = char
            
            if mapping.get(char, '') != word or reverse.get(word, '') != char:
                return False

        return True