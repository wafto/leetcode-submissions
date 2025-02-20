class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        def effort_bfs(effort: int) -> bool:
            queue = deque([(0, 0)])
            seen = {(0, 0)}

            while queue:
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in seen:
                        continue
                    diff = abs(heights[r][c] - heights[nr][nc])
                    if diff > effort:
                        continue
                    seen.add((nr, nc))
                    queue.append((nr, nc))
            return False

        left, right = 0, 0

        for r in range(rows):
            for c in range(cols):
                right = max(right, heights[r][c])

        while left <= right:
            mid = (right + left) // 2
            if effort_bfs(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
                
