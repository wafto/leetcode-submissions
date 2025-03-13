class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        if neg:
            x = -x

        queue = deque()
        while x > 0:
            queue.append(x % 10)
            x //= 10

        ans, n = 0, len(queue)
        for i in range(n):
            ans += queue[i] * (10 ** (n - i - 1))

        if ans >= (2 ** 31) - 1:
            return 0

        return -ans if neg else ans
        
            
        