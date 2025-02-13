class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)

        def distance(a: List[int], b: List[int]) -> float:
            return math.sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2))

        for i in range(n):
            for j in range(i + 1, n):
                dist = distance(bombs[i], bombs[j])
                if bombs[i][2] >= dist:
                    graph[i].append(j)
                if bombs[j][2] >= dist:
                    graph[j].append(i)
        
        def bfs(start: int) -> int:
            queue = deque([start])
            seen = {start}
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        queue.append(neighbor) 
                        seen.add(neighbor)
            return len(seen)

        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
        
        return ans


                