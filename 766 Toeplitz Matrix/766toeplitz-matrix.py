class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r - 1][c - 1] != matrix[r][c]:
                    return False

        return True