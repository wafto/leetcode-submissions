class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        output = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        visited = set()
        distance = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    output[r][c] = 0
                    visited.add((r, c))

        while queue:
            distance += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visited:
                        continue
                    output[nr][nc] = distance
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        return output







