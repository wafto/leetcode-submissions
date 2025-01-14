class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = defaultdict(int)
        output = 0

        for w, h in rectangles:
            ratios[w/h] += 1

        for cnt in ratios.values():
            output += (cnt * (cnt - 1)) // 2

        return output

