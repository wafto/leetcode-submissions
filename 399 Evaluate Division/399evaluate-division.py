class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]
            graph[a][b] = v
            graph[b][a] = 1 / v

        def bfs(src: str, dst: str) -> float:
            if src not in graph or dst not in graph:
                return -1

            queue = deque([(src, 1)])
            seen = {src}

            while queue:
                node, factor = queue.popleft()
                if node == dst:
                    return factor
                for neighbor, val in graph[node].items():
                    if neighbor in seen:
                        continue
                    queue.append((neighbor, factor * val))
                    seen.add(neighbor)
            
            return -1

        ans = []
        for src, dst in queries:
            ans.append(bfs(src, dst))

        return ans

