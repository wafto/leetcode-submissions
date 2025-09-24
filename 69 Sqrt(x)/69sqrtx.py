class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x

        while L <= R:
            M = (R + L) // 2
            C = M * M

            if C == x:
                return M

            if C > x:
                R = M - 1
            else:
                L = M + 1

        return R