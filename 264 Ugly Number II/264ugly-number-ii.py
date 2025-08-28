class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set([1])
        curr = None

        for _ in range(n):
            curr = heappop(heap)

            for prime in [2, 3, 5]:
                nxt = curr * prime
                if nxt in seen:
                    continue
                heappush(heap, nxt)
                seen.add(nxt)

        return curr

        # heap -> [1]
        # heap -> [2, 3, 5]
        # heap -> [3, 5, 4, 6, 10]
        # heap -> [9, 15, 5, 4, 6, 10]
        # heap -> [8, 12, 20, 9, 15, 5, 6, 10]
        # heap -> [8, 12, 20, 9, 15, 6, 10, 25]