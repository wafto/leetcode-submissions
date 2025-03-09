class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bits = x ^ y
        ans = 0
        
        while bits > 0:
            ans += bits & 1
            bits >>= 1

        return ans