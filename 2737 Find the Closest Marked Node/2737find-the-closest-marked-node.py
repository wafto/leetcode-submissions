class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        graph = defaultdict(list)
        shortest = dict()
        marked = set(marked)

        for u, v, w in edges:
            graph[u].append((v, w))

        heap = [(0, s)]

        while heap:
            weight, node = heapq.heappop(heap)

            if node in shortest:
                continue

            shortest[node] = weight

            if node in marked:
                return weight

            for nei, weight2 in graph[node]:
                if nei in shortest:
                    continue
                heapq.heappush(heap, (weight + weight2, nei))

        return -1

        
        