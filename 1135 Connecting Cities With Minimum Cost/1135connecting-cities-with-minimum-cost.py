class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x, y, c in connections:
            graph[x].append((y, c))
            graph[y].append((x, c))

        heap = [(0, 1)]
        seen = set()
        ans = 0

        while heap:
            cost, node = heappop(heap)

            if node in seen:
                continue

            seen.add(node)
            ans += cost

            for nei, ncost in graph[node]:
                if nei in seen:
                    continue
                heappush(heap, (ncost, nei))

        return -1 if len(seen) != n else ans