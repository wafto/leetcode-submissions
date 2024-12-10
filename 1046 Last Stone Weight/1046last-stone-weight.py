class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            res = abs(s1 - s2) * -1
            heapq.heappush(stones, res)
        return abs(stones[0]) if stones else 0