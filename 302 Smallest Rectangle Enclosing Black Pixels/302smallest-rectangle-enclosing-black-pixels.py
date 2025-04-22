class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows, cols = len(image), len(image[0])
        left, right, top, bottom = y, y, x, x

        for r in range(rows):
            for c in range(cols):
                if image[r][c] == '1':
                    top = min(top, r)
                    bottom = max(bottom, r)

                    left = min(left, c)
                    right = max(right, c)
                    
        return (right - left + 1) * (bottom - top + 1)
