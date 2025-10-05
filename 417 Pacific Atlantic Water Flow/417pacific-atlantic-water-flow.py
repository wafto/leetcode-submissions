class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = 0, 1

        queue = {pacific: deque(), atlantic: deque()}
        visited = {pacific: set(), atlantic: set()}

        for c in range(cols):
            queue[pacific].append((0, c))
            visited[pacific].add((0, c))

        for r in range(1, rows):
            queue[pacific].append((r, 0))
            visited[pacific].add((r, 0))

        for c in range(cols):
            queue[atlantic].append((rows - 1, c))
            visited[atlantic].add((rows - 1, c))
        
        for r in range(rows - 1):
            queue[atlantic].append((r, cols - 1))
            visited[atlantic].add((r, cols - 1))
            
        def bfs(ocean: int) -> None:
            while queue[ocean]:
                r, c = queue[ocean].popleft()

                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if nr in [-1, rows] or nc in [-1, cols] or (nr, nc) in visited[ocean]:
                        continue
                    if heights[r][c] <= heights[nr][nc]:
                        queue[ocean].append((nr, nc))
                        visited[ocean].add((nr, nc))

        bfs(pacific)
        bfs(atlantic)

        return list(visited[pacific] & visited[atlantic])