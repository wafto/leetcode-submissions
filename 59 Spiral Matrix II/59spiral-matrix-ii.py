class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        count, limit = 0, n * n
        
        up, down, left, right = 0, n - 1, 0, n - 1

        while count < limit:
            # from left to right
            for c in range(left, right + 1):
                count += 1
                matrix[up][c] = count

            # from up to down
            for r in range(up + 1, down + 1):
                count += 1
                matrix[r][right] = count

            # from right to left
            if up != down:
                for c in range(right - 1, left - 1, -1):
                    count += 1
                    matrix[down][c] = count

            # from down to up
            if left != right:
                for r in range(down - 1, up, -1):
                    count += 1
                    matrix[r][left] = count

            up, down, left, right = up + 1, down - 1, left + 1, right - 1

        return matrix