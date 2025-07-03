class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        m = n * 3
        img = [[0] * m for _ in range(m)]
        
        for r in range(n):
            for c in range(n):
                img[r + n][c + n] = img2[r][c]

        def overlap(r: int, c: int) -> int:
            count = 0
            for r2 in range(n):
                for c2 in range(n):
                    if img1[r2][c2] == 1 and img[r + r2][c + c2] == 1:
                        count += 1
            return count

        largest = 0

        for r in range(1, m - n):
            for c in range(1, m - n):
                largest = max(largest, overlap(r, c))

        return largest


