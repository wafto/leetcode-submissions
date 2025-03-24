class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_end = 0

        for start, end in meetings:
            start = max(start, prev_end + 1)
            days -= max(0, end - start + 1)
            prev_end = max(prev_end, end)

        return days