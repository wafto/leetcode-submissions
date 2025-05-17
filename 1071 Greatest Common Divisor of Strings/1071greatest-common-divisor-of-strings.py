class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        n, m = len(str1), len(str2)
        g = gcd(n, m)
        p = str1[: g]

        if p * (n // g) == str1 and p * (m // g) == str2:
            return p

        return ''


        