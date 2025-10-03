class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        memo = {}
    
        def dp(a: int, b: int) -> bool:
            c = a + b

            if (a, b) in memo:
                return memo[(a, b)]

            if c == n3:
                return True

            ans = False

            if a < n1 and s1[a] == s3[c]:
                ans = ans or dp(a + 1, b)

            if b < n2 and s2[b] == s3[c]:
                ans = ans or dp(a, b + 1) 

            memo[(a, b)] = ans
            return memo[(a, b)]

        if n1 + n2 != n3:
            return False

        return dp(0, 0)
