class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED = 0
        BLUE = 1
        
        ans = [float('inf')] * n
        graph = {RED: defaultdict(list), BLUE: defaultdict(list)}

        for u, v in redEdges:
            graph[RED][u].append(v)

        for u, v in blueEdges:
            graph[BLUE][u].append(v)

        queue = deque([(0, RED, 0), (0, BLUE, 0)]) # (node, color, steps)
        seen = {(0, RED), (0, BLUE)}

        while queue:
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node], steps)

            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) in seen:
                    continue
                queue.append((neighbor, 1 - color, steps + 1))
                seen.add((neighbor, 1 - color))

        for i in range(n):
            if ans[i] == float('inf'):
                ans[i] = -1

        return ans    

