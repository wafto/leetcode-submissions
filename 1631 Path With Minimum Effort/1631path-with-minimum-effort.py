class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        heap = [(0, 0, 0)] # effort, row, col
        efforts = {}

        while heap:
            e, r, c, = heappop(heap)

            if (r, c) in efforts:
                continue

            efforts[(r, c)] = e

            if (rows - 1, cols - 1) in efforts:
                return efforts[(rows - 1, cols - 1)]

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in efforts:
                    continue

                ne = max(e, abs(heights[r][c] - heights[nr][nc]))

                heappush(heap, (ne, nr, nc))

        #return efforts[(rows - 1, cols - 1)]


            