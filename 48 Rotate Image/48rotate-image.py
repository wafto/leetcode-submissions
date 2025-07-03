class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        top, down = 0, n - 1
        while top < down:
            matrix[top], matrix[down] = matrix[down], matrix[top]
            top, down = top + 1, down - 1
        
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]