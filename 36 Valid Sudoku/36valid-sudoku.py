class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = set(), set(), set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue

                if (num, r) in rows or (num, c) in cols or (num, r // 3, c // 3) in squares:
                    return False

                rows.add((num, r))
                cols.add((num, c))
                squares.add((num, r // 3, c // 3))

        return True
        