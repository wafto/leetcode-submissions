class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        blue, red = 0, 1
        graph = [defaultdict(list), defaultdict(list)]

        for u, v in redEdges:
            graph[red][u].append(v)

        for u, v in blueEdges:
            graph[blue][u].append(v)

        queue = deque([(0, 0, blue), (0, 0, red)]) # (steps, node, color)
        visited = set([(0, 0, blue), (0, 0, red)])
        shortest = [float('inf')] * n

        while queue:
            steps, node, color = queue.popleft()
            
            shortest[node] = min(shortest[node], steps)

            for nei in graph[color][node]:
                if (nei, 1 - color) in visited:
                    continue
                queue.append((steps + 1, nei, 1 - color))
                visited.add((nei, 1 - color))
        
        for i in range(len(shortest)):
            shortest[i] = -1 if shortest[i] == float('inf') else shortest[i]

        return shortest
