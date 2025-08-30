class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        ans = []

        for i in range(rows + cols - 1):
            r = 0 if i < cols - 1 else i - (cols - 1)
            c = i if i < cols - 1 else cols - 1

            tmp = []
            while r < rows and c >= 0:
                tmp.append(mat[r][c])
                r, c = r + 1, c - 1

            if i & 1 == 0:
                tmp.reverse()

            ans.extend(tmp)

        return ans
