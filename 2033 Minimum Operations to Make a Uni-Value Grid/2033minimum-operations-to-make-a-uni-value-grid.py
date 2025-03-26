class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        rows, cols = len(grid), len(grid[0])
        data, total = [], 0
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] % x != grid[0][0] % x:
                    return -1
                data.append(grid[r][c])
                total += grid[r][c]

        data.sort()
        prefix = 0
        ans = float('inf')

        for i in range(len(data)):
            left = data[i] * i - prefix
            right = total - prefix - (data[i] * (len(data) - i))
            ans = min(ans, (right + left) // x)
            prefix += data[i]

        return ans
        