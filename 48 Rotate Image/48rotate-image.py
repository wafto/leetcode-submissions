class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        top, bottom = 0, n - 1
        while top < bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top, bottom = top + 1, bottom - 1

        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                