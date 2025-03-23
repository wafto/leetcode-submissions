class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        MOD = (10 ** 9) + 7
        heap = [(0, 0)] # weight, node
        cost = [float('inf')] * n
        paths = [0] * n
        paths[0] = 1

        while heap:
            weight, node = heapq.heappop(heap)
            
            for nei, nei_weight in graph[node]:
                new_weight = weight + nei_weight

                if new_weight < cost[nei]:
                    cost[nei] = new_weight
                    paths[nei] = paths[node]
                    heapq.heappush(heap, (new_weight, nei))
                elif new_weight == cost[nei]:
                    paths[nei] = (paths[nei] + paths[node]) % MOD

        return paths[n - 1]

