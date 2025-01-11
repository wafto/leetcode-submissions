class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        size = len(s)

        if size < k:
            return False
        
        if size == k:
            return True

        freq = defaultdict(int)
        for c in s: 
            freq[c] += 1

        odds = 0
        for c in freq.values():
            odds += 1 if c & 1 == 1 else 0
        
        return odds <= k