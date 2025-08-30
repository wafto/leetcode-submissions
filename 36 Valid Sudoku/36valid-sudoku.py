class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for r in range(9):
            freq = [0] * 9
            for c in range(9):
                if board[r][c].isnumeric():
                    freq[int(board[r][c]) - 1] += 1
                    if freq[int(board[r][c]) - 1] > 1:
                        return False

        # cols
        for c in range(9):
            freq = [0] * 9
            for r in range(9):
                if board[r][c].isnumeric():
                    freq[int(board[r][c]) - 1] += 1
                    if freq[int(board[r][c]) - 1] > 1:
                        return False

        # squares
        def valid_square(r: int, c: int) -> bool:
            freq = [0] * 9
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j].isnumeric():
                        freq[int(board[i][j]) - 1] += 1
                        if freq[int(board[i][j]) - 1] > 1:
                            return False
            return True

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not valid_square(r, c):
                    return False

        return True