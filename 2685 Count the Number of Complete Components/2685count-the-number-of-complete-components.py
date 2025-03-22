class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        seen = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(node: int) -> List[int]:
            queue = deque([node])
            seen.add(node)
            group = []

            while queue:
                nd = queue.popleft()
                group.append(nd)
                for nei in graph[nd]:
                    if nei in seen:
                        continue
                    queue.append(nei)
                    seen.add(nei)
            return group

        ans = 0
        
        for i in range(n):
            if i not in seen:
                group = bfs(i)
                if all([len(graph[node]) == len(group) - 1 for node in group]):
                    ans += 1

        return ans
            