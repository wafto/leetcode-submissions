class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            return 1 / self.myPow(x, -n)

        half = self.myPow(x, n // 2)

        return (half * half * x) if n & 1 else (half * half)