class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flipable = (a | b) ^ c
        ans = 0

        while flipable != 0:
            if flipable & 1:
                ax = a & 1
                bx = b & 1
                if c & 1:
                    ans += 0 if (ax or bx) else 1
                else:
                    ans += ax + bx
            a >>= 1
            b >>= 1
            c >>= 1            
            flipable >>= 1

        return ans