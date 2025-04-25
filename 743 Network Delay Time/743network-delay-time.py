class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        minheap = [(0, k)]
        shortest = {}

        while minheap:
            weight, node = heapq.heappop(minheap)

            if node in shortest:
                continue

            shortest[node] = weight

            for nei_node, nei_weight in graph[node]:
                if nei_node not in shortest:
                    heapq.heappush(minheap, (weight + nei_weight, nei_node))

        return -1 if len(shortest) != n else max(shortest.values())

