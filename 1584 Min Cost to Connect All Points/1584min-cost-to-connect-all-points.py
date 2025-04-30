class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        mincost = 0
        seen = set()

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((j, cost))
                graph[j].append((i, cost))

        minheap = []
        for dst, cost in graph[0]:
            heapq.heappush(minheap, (cost, 0, dst))

        seen.add(0)

        while minheap:
            cost, src, dst = heapq.heappop(minheap)

            if dst in seen:
                continue

            mincost += cost
            seen.add(dst)

            for nei_node, nei_cost in graph[dst]:
                if nei_node in seen:
                    continue
                heapq.heappush(minheap, (nei_cost, dst, nei_node))

        return mincost

        


