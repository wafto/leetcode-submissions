class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-num for num in piles]
        heapq.heapify(piles)

        for _ in range(k):
            pile = abs(heapq.heappop(piles))
            pile = pile - (pile // 2)
            heapq.heappush(piles, -pile)

        return -sum(piles)
