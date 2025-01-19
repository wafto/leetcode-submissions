class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])

        heap = []
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    heappush(heap, (heightMap[r][c], r, c))
                    visited.add((r, c))

        res, maxheight = 0, 0
        
        while heap:
            h, r, c = heappop(heap)
            maxheight = max(maxheight, h)
            res += maxheight - h

            neighbors = [[r + 1, c], [r - 1, c], [r, c - 1], [r, c + 1]]

            for nr, nc in neighbors:
                if nr in [-1, rows] or nc in [-1, cols] or (nr, nc) in visited:
                    continue
                heappush(heap, (heightMap[nr][nc], nr, nc))
                visited.add((nr, nc))

        return res



