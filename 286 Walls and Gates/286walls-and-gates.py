class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            seen = set([(r, c)])
            dist = 1

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in seen:
                            continue
                        if rooms[nr][nc] == -1 or rooms[nr][nc] == 0:
                            continue
                        seen.add((nr, nc))
                        rooms[nr][nc] = min(rooms[nr][nc], dist)
                        queue.append((nr, nc))
                dist += 1

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    bfs(r, c)

        return rooms 


        