class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashset, n, maximal = set(arr), len(arr), 0

        for i in range(n):
            for j in range(i + 1, n):
                prev, curr = arr[i], arr[j]
                size = 2

                while prev + curr in hashset:
                    size += 1
                    maximal = max(maximal, size)
                    prev, curr = curr, prev + curr

        return maximal
            