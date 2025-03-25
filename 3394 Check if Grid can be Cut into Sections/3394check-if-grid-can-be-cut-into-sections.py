class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles]
        y = [(r[1], r[3]) for r in rectangles]

        def can_be_cutted(intervals: List[int]) -> bool:
            count = 0
            prev_end = 0
            for start, end in intervals:
                if start >= prev_end:
                    count += 1
                    if count >= 3:
                        return True
                prev_end = max(prev_end, end)
            return False

        x.sort()

        if can_be_cutted(x):
            return True

        y.sort()

        if can_be_cutted(y):
            return True

        return False

