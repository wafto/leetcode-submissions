class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m, c = len(a), len(b), 0
        ans = []

        for i in range(max(n, m)):
            ai = int(a[n - 1 - i]) if n - 1 - i >= 0 else 0
            bi = int(b[m - 1 - i]) if m - 1 - i >= 0 else 0
            num = ai + bi + c

            if num == 3:
                ans.append('1')
            elif num == 2:
                ans.append('0')
                c = 1
            elif num == 1:
                ans.append('1')
                c = 0
            else:
                ans.append('0')

        if c:
            ans.append('1')

        ans.reverse()
        
        return ''.join(ans)
            


