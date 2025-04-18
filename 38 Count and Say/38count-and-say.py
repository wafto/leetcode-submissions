class Solution:
    def countAndSay(self, n: int) -> str:
        curr = '1'

        for _ in range(n - 1):
            nxt, j, k = '', 0, 0
            
            while j < len(curr):
                while k < len(curr) and curr[k] == curr[j]:
                    k += 1
                nxt += str(k - j) + curr[j]
                j = k
            
            curr = nxt

        return curr



        

        