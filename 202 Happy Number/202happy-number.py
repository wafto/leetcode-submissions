class Solution:
    def isHappy(self, n: int) -> bool:
        
        def digits(n: int) -> List[int]:
            ans = []
            while n > 0:
                ans.append(n % 10)
                n //= 10
            return ans

        seen = set()

        while True:
            acc = 0
            for d in digits(n):
                acc += d ** 2
            if acc == 1:
                return True
            if acc in seen:
                break
            seen.add(acc)
            n = acc

        return False
            

