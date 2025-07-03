class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        flatten = []

        if rows * cols != r * c:
            return mat

        for row in range(rows):
            for col in range(cols):
                flatten.append(mat[row][col])

        reshape = [[0] * c for _ in range(r)]
        index = 0

        for row in range(r):
            for col in range(c):
                reshape[row][col] = flatten[index]
                index += 1

        return reshape