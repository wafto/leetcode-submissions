class Solution:
    def hammingWeight(self, n: int) -> int:
        
        @cache
        def hamming(n: int) -> int: 
            if n <= 0:
                return 0
            return hamming(n >> 1) + (n & 1)

        return hamming(n)

