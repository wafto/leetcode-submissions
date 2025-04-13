class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def pow(x: int, n: int) -> int:
            if n == 0:
                return 1
            res = 1
            while n > 1:
                if n & 1:
                    res = (res * x) % MOD
                n = n // 2
                x = (x * x) % MOD
            return res * x

        even = ceil(n / 2)
        odd = n // 2

        return (pow(5, even) * pow(4, odd)) % MOD