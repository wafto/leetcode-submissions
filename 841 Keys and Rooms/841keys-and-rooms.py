class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        graph = {i: rooms[i] for i in range(n)}
        seen = set([0])
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)

        return len(seen) == n



        