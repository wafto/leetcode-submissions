class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        prev = intervals[0]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] >= curr[0]:
                prev[1] = max(prev[1], curr[1])
            else:
                merged.append(prev)
                prev = curr

        merged.append(prev)
        
        return merged

