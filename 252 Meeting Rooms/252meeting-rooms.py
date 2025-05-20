class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted([(r[0], r[1]) for r in intervals])

        if not intervals:
            return True

        last = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < last:
                return False
            last = max(last, end)

        return True

