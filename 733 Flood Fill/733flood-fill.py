class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])

        starting_color = image[sr][sc]

        def dfs(r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= rows or c >= cols: 
                return

            if image[r][c] != starting_color or image[r][c] == color:
                return
            
            image[r][c] = color

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                dfs(nr, nc)

        dfs(sr, sc)
        
        return image 