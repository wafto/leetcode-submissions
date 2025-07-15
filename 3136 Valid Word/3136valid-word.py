class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        if n < 3:
            return False

        vowel, consonant = False, False

        for c in word:
            if c.isdigit():
                continue

            c = c.lower()

            if ord(c) < ord('a') or ord(c) > ord('z'):
                return False

            if c in vowels:
                vowel = True
            else:
                consonant = True

        return vowel and consonant
           