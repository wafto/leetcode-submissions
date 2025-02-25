class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, n = len(board), len(board[0]), len(word)

        if rows * cols < n:
            return False

        def backtracking(r: int, c: int, i: int, used: Set[tuple]) -> bool:
            if i == n:
                return True

            for nr, nc in [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]:
                if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in used or board[nr][nc] != word[i]:
                    continue
                
                used.add((nr, nc))
                
                if backtracking(nr, nc, i + 1, used):
                    return True
                
                used.remove((nr, nc))
            
            return False
                
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c] and backtracking(r, c, 1, {(r, c)}):
                    return True

        return False
