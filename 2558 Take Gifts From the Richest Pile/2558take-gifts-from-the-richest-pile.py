class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)

        while k > 0:
            gift = -heapq.heappop(heap)
            reduced = -int(math.sqrt(gift))
            heapq.heappush(heap, reduced)
            k -= 1

        return -sum(heap)
        
            
