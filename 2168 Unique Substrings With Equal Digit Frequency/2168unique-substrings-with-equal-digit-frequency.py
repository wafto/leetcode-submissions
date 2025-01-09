class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        uniques = set()
        size = len(s)
     
        for i in range(size):
            counter = defaultdict(lambda: 0)
            total, mx = 0, 0
            for j in range(i, size):
                counter[s[j]] += 1
                mx = max(mx, counter[s[j]])
                total += 1
                if len(counter) * mx == total:
                    uniques.add(s[i: j + 1])
        return len(uniques)
                