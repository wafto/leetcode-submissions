class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        seen = {start}


        while queue:
            node = queue.popleft()

            if node < 0 or node >= n:
                continue

            if arr[node] == 0:
                return True
            
            for nei in [node + arr[node], node - arr[node]]:
                if nei in seen:
                    continue
                queue.append(nei)
                seen.add(nei)

        return False
            