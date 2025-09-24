class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n, heap = len(heights), []

        for i in range(n - 1):
            climb = heights[i + 1] - heights[i]

            if climb <= 0:
                continue
            
            heappush(heap, climb)
            
            if len(heap) <= ladders:
                continue
                
            bricks -= heappop(heap)
            
            if bricks < 0:
                return i
            
        return n - 1
            
             