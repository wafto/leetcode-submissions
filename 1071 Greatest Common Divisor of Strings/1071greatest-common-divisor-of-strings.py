class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        smallest = str1 if n1 < n2 else str2
        
        def valid(i: int) -> bool:
            if n1 % i or n2 % i:
                return False
            sub = smallest[:i]
            d1, d2 = n1 // i, n2 // i

            return str1 == sub * d1 and str2 == sub * d2

        for i in range(min(n1, n2), 0, -1):
            if valid(i):
                return smallest[:i]
        
        return ''

        
