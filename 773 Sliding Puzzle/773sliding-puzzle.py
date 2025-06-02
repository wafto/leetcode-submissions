class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = tuple([cell for row in board for cell in row])
        graph = {
            0: [1, 3],
            1: [0, 4, 2],
            2: [1, 5],
            3: [0, 4],
            4: [3, 1, 5],
            5: [2, 4],
        }

        queue = deque([(board, board.index(0))])
        visited = set([board])
        moves = 0

        # BFS
        while queue:
            for _ in range(len(queue)):
                state, pos = queue.popleft()

                if state == (1, 2, 3, 4, 5, 0):
                    return moves

                original = list(state)

                for nei in graph[pos]:
                    copy = original.copy()
                    copy[nei], copy[pos] = copy[pos], copy[nei]
                    copy = tuple(copy)
                    
                    if copy in visited:
                        continue

                    queue.append((copy, nei))
                    visited.add(copy)
                    
            moves += 1
        
        return -1