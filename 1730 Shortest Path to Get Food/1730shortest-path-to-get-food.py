class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        steps = 0

        start = None
        foods = set()

        for r in range(rows):
            for c in range(cols):
                cell = (r, c)
                if grid[r][c] == '*':
                    start = cell
                elif grid[r][c] == '#':
                    foods.add(cell)
                elif grid[r][c] == 'X':
                    visited.add(cell)
                else:
                    pass

        if not start or not foods:
            return -1

        queue.append(start)
        visited.add(start)

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                if (r, c) in foods:
                    return steps
               
                if r - 1 >= 0 and (r - 1, c) not in visited:
                    queue.append((r - 1, c))
                    visited.add((r - 1, c))
                    
                if r + 1 < rows and (r + 1, c) not in visited:
                    queue.append((r + 1, c))
                    visited.add((r + 1, c))
                
                if c - 1 >= 0 and (r, c - 1) not in visited:
                    queue.append((r, c - 1))
                    visited.add((r, c - 1))
                
                if c + 1 < cols and (r, c + 1) not in visited:
                    queue.append((r, c + 1))
                    visited.add((r, c + 1))

                visited.add((r, c))
            steps += 1

        return -1


        
                

                
                


