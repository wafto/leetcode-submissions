class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans, n = 0, len(points)

        def area(p1, p2, p3) -> float:
            x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    ans = max(ans, area(points[i], points[j], points[k]))
            
        return ans