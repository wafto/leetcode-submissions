class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i, ans = 0, []

        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            start = min(newInterval[0], intervals[i][0])
            end = max(newInterval[1], intervals[i][1])
            newInterval = [start, end]
            i += 1
        
        ans.append(newInterval)

        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans
    