class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = (0, 0)
        visited = set([pos])
        
        for p in path:
            if p == 'N':
                pos = (pos[0] + 1, pos[1])
            elif p == 'S':
                pos = (pos[0] - 1, pos[1])
            elif p == 'E':
                pos = (pos[0], pos[1] + 1)
            else:
                pos = (pos[0], pos[1] - 1)
            if pos in visited:
                return True
            visited.add(pos)

        
        return False

