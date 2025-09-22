class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        graph = {
            '0': ['9', '1'],
            '1': ['0', '2'],
            '2': ['1', '3'],
            '3': ['2', '4'],
            '4': ['3', '5'],
            '5': ['4', '6'],
            '6': ['5', '7'],
            '7': ['6', '8'],
            '8': ['7', '9'],
            '9': ['8', '0'],
        }

        def posibilities(lock: str) -> List[str]:
            ans = []
            for i in range(4):
                copy = list(lock)
                for neighbor in graph[lock[i]]:
                    copy[i] = neighbor
                    tmp = ''.join(copy)
                    if tmp in deadends:
                        continue
                    ans.append(tmp)
            return ans

        def bfs(current: str) -> int:
            steps = 0
            queue = deque()
            seen = set()

            if current not in deadends:
                queue.append(current)
                seen.add(current)

            while queue:
                for _ in range(len(queue)):
                    last = queue.popleft()

                    if last == target:
                        return steps

                    for posibility in posibilities(last):
                        if posibility in seen:
                            continue
                        seen.add(posibility)
                        queue.append(posibility)

                steps += 1

            return -1

        return bfs('0000')