class Solution:
    def reverse(self, x: int) -> int:
        output = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)

        if output > (2 ** 31) - 1 or output < -2 ** 31:
            return 0

        return output