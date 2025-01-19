class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hm = defaultdict(int)

        for c in s:
            hm[c] += 1

        return len(set(hm.values())) == 1
        
        
        