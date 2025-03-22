class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        ans = 0
        
        while num > 0:
            ans += num & 1
            num >>= 1
            
        return ans
    