class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
    
        def dfs(r: int, c: int) -> bool:
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return False
            grid[r][c] = 'x'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            return True
            
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j):
                    islands += 1
        
        return islands
        

            