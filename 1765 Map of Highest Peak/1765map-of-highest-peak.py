class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        ans = [[-1 for c in range(cols)] for r in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    ans[r][c] = 0
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            h = ans[r][c]

            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for nr, nc in neighbors:
                if nr < 0 or nc < 0 or nr == rows or nc == cols or ans[nr][nc] != -1:
                    continue
                ans[nr][nc] = h + 1
                queue.append((nr, nc))

        return ans

