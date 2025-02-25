class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
            
        if n < 4:
            return 0

        # cols, diagonal and adiagonal are the occupied ones
        def backtracking(row: int, cols: Set[int], diagonal: Set[int], adiagonal: Set[int]) -> int:
            if row == n:
                return 1

            solutions = 0
            
            for col in range(n):
                if col in cols or (row - col) in diagonal or (row + col) in adiagonal:
                    continue
                
                cols.add(col)
                diagonal.add(row - col)
                adiagonal.add(row + col)

                solutions += backtracking(row + 1, cols, diagonal, adiagonal)

                cols.remove(col)
                diagonal.remove(row - col)
                adiagonal.remove(row + col)

            return solutions
                
        return backtracking(0, set(), set(), set())

            
