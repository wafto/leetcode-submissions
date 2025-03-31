class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda p: p[1])
        arrows, prev_end = 1, points[0][1]

        for start, end in points:
            if prev_end < start:
                arrows += 1
                prev_end = end

        return arrows

