class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1]]

        for i in range(1, numRows):
            size = i + 1
            level = [1] * size

            if size > 2:
                for j in range(1, size - 1):
                    level[j] = tri[-1][j - 1] + tri[-1][j] 

            tri.append(level)

        return tri

