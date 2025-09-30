class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        seen = set()

        @cache
        def dfs(r: int, c: int) -> int:
            seen.add((r, c))
            longest = 1

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in seen:
                    continue

                if matrix[nr][nc] <= matrix[r][c]:
                    continue

                longest = max(longest, dfs(nr, nc) + 1)
                
            seen.remove((r, c))
            return longest

        largest = 0

        for r in range(rows):
            for c in range(cols):
                largest = max(largest, dfs(r, c))

        return largest