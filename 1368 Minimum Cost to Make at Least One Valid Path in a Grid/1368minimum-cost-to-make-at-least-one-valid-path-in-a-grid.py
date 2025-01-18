class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = {
            1: [0, 1],
            2: [0, -1],
            3: [1, 0],
            4: [-1, 0],
        }
        queue = deque([(0, 0, 0)])
        mincost = {(0, 0): 0}

        while queue:
            r, c, cost = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return cost

            for d in dirs:
                rx, cx = dirs[d]
                rn, cn = r + rx, c + cx
                ncost = cost if grid[r][c] == d else (cost + 1)

                if rn < 0 or cn < 0 or rn >= rows or cn >= cols:
                    continue

                if ncost >= mincost.get((rn, cn), float('inf')):
                    continue

                if grid[r][c] == d:
                    queue.appendleft((rn, cn, ncost))
                else:
                    queue.append((rn, cn, ncost))

                mincost[(rn, cn)] = ncost

                 


        