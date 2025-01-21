class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        ans = 0
        
        for stone in stones:
            ans += 1 if stone in jewels else 0

        return ans