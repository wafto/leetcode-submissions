class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        heap, ops, ps = [], 0, 0

        for num in nums:
            if num < 0:
                heapq.heappush(heap, num)

            ps += num

            if ps < 0:
                ps -= heapq.heappop(heap)
                ops += 1

        return ops