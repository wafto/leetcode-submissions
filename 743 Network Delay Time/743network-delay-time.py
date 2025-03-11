class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(n + 1)}

        for u, v, w in times:
            adj[u].append((v, w))

        minheap = [(0, k)]
        shortest = defaultdict(int)

        while minheap:
            cost, node = heapq.heappop(minheap)
            
            if node in shortest:
                continue
            
            shortest[node] = cost

            for v, w in adj[node]:
                if v not in shortest:
                    heapq.heappush(minheap, (cost + w, v))

        if len(shortest) != n:
            return -1

        return max(shortest.values())
        