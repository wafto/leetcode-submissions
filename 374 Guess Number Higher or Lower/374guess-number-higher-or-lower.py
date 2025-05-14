# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 1, n

        while L <= R:
            M = (R + L) // 2
            G = guess(M)

            if G == 0:
                return M

            if G == 1:
                L = M + 1
            else:
                R = M - 1
