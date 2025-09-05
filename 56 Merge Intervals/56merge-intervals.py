class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        start, end = intervals[0]

        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                ans.append([start, end])
                start, end = intervals[i]

        ans.append([start, end])

        return ans

