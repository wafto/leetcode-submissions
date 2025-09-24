class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []
        ans, count = 0, 0
        
        for s, e in intervals:
            heappush(starts, s)
            heappush(ends, e)
            
        while starts:
            if starts[0] < ends[0]:
                heappop(starts)
                count += 1
            else:
                heappop(ends)
                count -= 1
            ans = max(ans, count)
            
        return ans
    