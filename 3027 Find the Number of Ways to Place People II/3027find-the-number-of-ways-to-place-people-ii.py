class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        points.sort(key=lambda point: (point[0], -point[1]))

        for a in range(n - 1):
            min_y = float('-inf')
            for b in range(a + 1, n):
                ay, by = points[a][1], points[b][1]
                if by > min_y and by <= ay:
                    count += 1
                    min_y = by

        return count