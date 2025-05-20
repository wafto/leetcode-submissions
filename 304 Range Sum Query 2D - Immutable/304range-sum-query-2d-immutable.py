class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.ps = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            ps = 0
            for c in range(cols):
                ps += matrix[r][c]
                self.ps[r + 1][c + 1] = ps + self.ps[r][c + 1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        br = self.ps[r2][c2]
        tr = self.ps[r1 - 1][c2]
        tl = self.ps[r1 - 1][c1 - 1]
        bl = self.ps[r2][c1 - 1]
        
        return br - tr - bl + tl        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)