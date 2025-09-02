class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count, n = 0, len(points)
        points.sort(key=lambda point: (point[0], -point[1]))

        for a in range(n - 1):
            bottom_right_y = -1
            for b in range(a + 1, n):
                ay = points[a][1]
                by = points[b][1]
                if by <= ay and by > bottom_right_y:
                    count += 1
                    bottom_right_y = by

        return count
                