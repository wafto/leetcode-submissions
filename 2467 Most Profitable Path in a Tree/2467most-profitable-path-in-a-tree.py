class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        path = dict() # bob's: node -> time
        maximal = float('-inf')

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # bob's pathing
        def dfs(node: int, prev: int, time: int) -> bool:
            if node == 0:
                return True
            for nei in graph[node]:
                if nei == prev:
                    continue
                if dfs(nei, node, time + 1):
                    path[node] = time
                    return True
            return False

        dfs(bob, -1, 0)
        
        # alice
        queue = deque([(0, -1, 0, amount[0])]) # (node, prev, time, amount)
        while queue:
            node, prev, time, income = queue.popleft()
            for nei in graph[node]:
                if nei == prev:
                    continue
                n_income = amount[nei]
                n_time = time + 1
                if nei in path:
                    b_time = path[nei]
                    if n_time > b_time:
                        n_income = 0
                    elif n_time == b_time:
                        n_income //= 2
                queue.append((nei, node, n_time, income + n_income))
                if len(graph[nei]) == 1:
                    maximal = max(maximal, income + n_income)
        
        return maximal





