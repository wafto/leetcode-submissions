class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n, res, j, last = len(events), 0, 0, max(e[1] for e in events)
        heap = []

        for i in range(1, last + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(heap, events[j][1])
                j += 1
            while heap and heap[0] < i:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                res += 1

        return res



        
