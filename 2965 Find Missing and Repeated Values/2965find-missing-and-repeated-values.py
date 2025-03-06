class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        mapping = {num: 0 for num in range(1, (n * n) + 1)}

        for r in range(n):
            for c in range(n):
                mapping[grid[r][c]] += 1

        miss, double = 0, 0

        for num, cnt in mapping.items():
            if cnt == 0:
                miss = num
            elif cnt == 2:
                double = num

        return [double, miss]


        

