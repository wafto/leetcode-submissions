class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        minheap = [(0, k)]
        shortest = {}

        while minheap:
            weight, node = heappop(minheap)

            if node in shortest:
                continue

            shortest[node] = weight

            for nnode, nweight in graph[node]:
                if nnode in shortest:
                    continue
                heappush(minheap, (nweight + weight, nnode))

        if len(shortest) < n:
            return -1

        return max(shortest.values())