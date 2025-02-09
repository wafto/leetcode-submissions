class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}

        def dfs(node: int):
            for room in rooms[node]:
                if room not in seen:
                    seen.add(room)
                    dfs(room)

        dfs(0)
        return len(seen) == len(rooms)
