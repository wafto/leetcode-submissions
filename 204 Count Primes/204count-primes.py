class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [False, False] + [True] * (n - 2)

        for i in range(2, int(sqrt(n)) + 1):
            if primes[i]:
                for j in range(i << 1, n, i):
                    primes[j] = False

        return sum(primes)