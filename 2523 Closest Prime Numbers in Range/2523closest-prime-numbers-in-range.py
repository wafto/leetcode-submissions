class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def get_primes() -> List[int]:
            primes = [True] * (right + 1)
            primes[0] = False
            primes[1] = False

            for i in range(2, int(sqrt(right)) + 1):
                if not primes[i]:
                    continue 
                for j in range(i + i, right + 1, i):
                    primes[j] = False

            ans = []
            for i in range(len(primes)):
                if primes[i] and i >= left:
                    ans.append(i)
            return ans

        data, smallest, res = get_primes(), right + 1, [-1, -1]

        for i in range(1, len(data)):
            if data[i] - data[i - 1] < smallest:
                smallest = data[i] - data[i - 1]
                res = [data[i - 1], data[i]]

        return res


