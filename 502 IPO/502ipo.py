class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        n, i, maxheap = len(projects), 0, []

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxheap, -projects[i][1])
                i += 1
            
            if not maxheap:
                return w

            w += -heapq.heappop(maxheap)

        return w
            
