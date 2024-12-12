class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        piles = [-n for n in gifts]
        heapq.heapify(piles)
        s = 0
        while s < k:
            choose = heapq.heappop(piles)
            behind = math.floor(math.sqrt(choose * -1))
            heapq.heappush(piles, behind * -1)
            s += 1
        remaining = 0
        for n in piles:
            remaining += n
        return abs(remaining)
         
