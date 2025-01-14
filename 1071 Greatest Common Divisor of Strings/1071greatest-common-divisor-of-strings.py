class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1, s2 = len(str1), len(str2)
        shortest = str2 if s2 < s1 else str1

        for i in range(len(shortest), 0, -1):
            gcd = shortest[:i]

            if s1 % len(gcd) != 0 or s2 % len(gcd) != 0:
                continue

            if not str1.startswith(gcd) or not str2.startswith(gcd):
                continue
            
            large = gcd * (max(s1, s2) // len(gcd))

            if large[:s1] == str1 and large[:s2] == str2:
                return gcd

        return ''





