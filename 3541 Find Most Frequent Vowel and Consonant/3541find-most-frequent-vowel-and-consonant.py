class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = defaultdict(int)
        consonants = defaultdict(int)

        for c in s:
            if c in 'aeiou':
                vowels[c] += 1
            else:
                consonants[c] += 1

        maxv, maxc = 0, 0
        
        for char, count in vowels.items():
            maxv = max(maxv, count)

        for char, count in consonants.items():
            maxc = max(maxc, count)

        return maxv + maxc