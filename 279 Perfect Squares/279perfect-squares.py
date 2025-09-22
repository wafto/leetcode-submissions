class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        for i in range(1, n + 1):
            num = i ** 2
            if num <= n:
                squares.append(num)
            elif num > n:
                break
        
        queue = deque(squares)
        seen = set(squares)
        steps = 1

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()

                if current == n:
                    return steps

                for square in squares:
                    total = square + current
                    if total <= n and total not in seen:
                        queue.append(total)
                        seen.add(total)

            steps += 1
