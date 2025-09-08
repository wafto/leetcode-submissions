class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rmap, cmap = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rmap.add(r)
                    cmap.add(c)

        for r in rmap:
            for c in range(cols):
                matrix[r][c] = 0

        for c in cmap:
            for r in range(rows):
                matrix[r][c] = 0
        
        