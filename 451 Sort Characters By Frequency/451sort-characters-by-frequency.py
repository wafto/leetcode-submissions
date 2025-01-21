class Solution:
    def frequencySort(self, s: str) -> str:
        data = sorted(list(Counter(s).items()), key=lambda t: t[1], reverse=True)
        chars = []
        
        for char, count in data:
            chars.extend([char] * count)

        return ''.join(chars)