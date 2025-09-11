class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(set)
        seen = set()

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)

        def dfs(node: int) -> None:
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        def bfs(node: int) -> None:
            queue = deque([node])

            while queue:
                curr = queue.popleft()
                for nei in graph[curr]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)

        ans = 0
        for node in range(n):
            if node not in seen:
                ans += 1
                seen.add(node)
                bfs(node)

        return ans
        
