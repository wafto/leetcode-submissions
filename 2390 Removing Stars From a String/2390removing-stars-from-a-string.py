class Solution:
    def removeStars(self, s: str) -> str:
        queue = deque()

        for c in s:
            if c != '*':
                queue.append(c)
                continue

            if queue:
                queue.pop()

        return ''.join(queue)


            


