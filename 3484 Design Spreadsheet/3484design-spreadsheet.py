class Spreadsheet:

    def __init__(self, rows: int):
        rows += 1
        self.rows = rows
        self.sheet = [[0] * 26 for _ in range(rows)] 

    def cellToCoords(self, cell: str) -> Tuple[int]:
        return (int(cell[1:]), ord(cell[0]) - ord('A'))

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.cellToCoords(cell)
        if row < self.rows and col < 26:
            self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self.cellToCoords(cell)
        if row < self.rows and col < 26:
            self.sheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+')
        
        if a.isnumeric() and b.isnumeric():
            return int(a) + int(b)

        if a.isnumeric():
            r, c = self.cellToCoords(b)
            if r < self.rows and c < 26:
                return int(a) + self.sheet[r][c]
            else:
                return int(a)

        if b.isnumeric():
            r, c = self.cellToCoords(a)
            if r < self.rows and c < 26:
                return int(b) + self.sheet[r][c]
            else:
                return int(b)

        ar, ac = self.cellToCoords(a)
        br, bc = self.cellToCoords(b)

        a_val = self.sheet[ar][ac] if ar < self.rows and ac < 26 else 0
        b_val = self.sheet[br][bc] if br < self.rows and bc < 26 else 0

        return a_val + b_val

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)