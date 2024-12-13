class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        neighbors = [
            (-1, -1), (-1,  0), (-1, 1),
            ( 0, -1),           ( 0, 1),
            ( 1, -1), ( 1,  0), ( 1, 1),
        ]

        rows, cols = len(grid), len(grid[0])
        queue = deque()

        if grid[0][0] == 0:
            queue.append((0, 0))
            grid[0][0] = 2
        else:
            return -1

        def queueNeighbors(r: int, c: int):
            for rn, cn in neighbors:
                r2 = r + rn
                c2 = c + cn
                if r2 < 0 or c2 < 0 or r2 >= rows or c2 >= cols or grid[r2][c2] != 0:
                    continue
                queue.append((r2, c2))
                grid[r2][c2] = 2

        path = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return path
                queueNeighbors(r, c)
            path += 1

        return -1

                
