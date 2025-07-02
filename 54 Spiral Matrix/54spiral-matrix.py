class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        size = rows * cols
        ans = []

        up, down, left, right = 0, rows - 1, 0, cols - 1

        while len(ans) < size:
            # from left to right
            for c in range(left, right + 1):
                ans.append(matrix[up][c])

            # from top to down
            for r in range(up + 1, down + 1):
                ans.append(matrix[r][right])

            # from right to left
            if up != down:
                for c in range(right - 1, left - 1, -1):
                    ans.append(matrix[down][c])

            # from down to up
            if left != right:
                for r in range(down - 1, up, -1):
                    ans.append(matrix[r][left])

            up, down, right, left = up + 1, down - 1, right - 1, left + 1

        return ans
