class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
            
        while n > 1:
            prev = n
            for f in [5, 3, 2]:
                if n % f == 0:
                    n //= f
                    break
            if n == prev:
                break

        return n in [1, 2, 3, 5]
        

