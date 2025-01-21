class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        hashmap = {}

        def mapkey(data: List[int]) -> Tuple:
            #return '|'.join(map(str, data))
            return tuple(data)

        for row in grid:
            key = mapkey(row)
            hashmap[key] = 1 + hashmap.get(key, 0)

        ans = 0

        for c in range(cols):
            col = [0] * cols
            for i in range(rows):
                col[i] = grid[i][c]
            key = mapkey(col)
            if key in hashmap:
                ans += hashmap[key]

        return ans








    