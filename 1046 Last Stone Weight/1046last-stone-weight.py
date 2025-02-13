class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            remain = abs(heapq.heappop(stones) - heapq.heappop(stones))
            heapq.heappush(stones, -remain)

        return -stones[0]
