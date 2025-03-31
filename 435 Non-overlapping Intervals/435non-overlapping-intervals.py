class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda arr: arr[1])
        prev, removed = float('-inf'), 0

        for start, end in intervals:
            if start < prev:
                removed += 1
            else:
                prev = max(prev, end)

        return removed
