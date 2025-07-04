class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        start = image[sr][sc]

        def dfs(r: int, c: int) -> None:
            image[r][c] = color

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or image[nr][nc] != start:
                    continue
                if image[nr][nc] == color:
                    continue
                dfs(nr, nc)

        dfs(sr, sc)

        return image
