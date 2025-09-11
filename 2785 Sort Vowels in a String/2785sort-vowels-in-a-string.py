class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        indexes = []

        for i, c in enumerate(s):
            if c in 'AEIOUaeiou':
                vowels.append(c)
                indexes.append(i)

        vowels.sort()
        s = list(s)
        j = 0

        for i in indexes:
            s[i] = vowels[j]
            j += 1

        return ''.join(s)
