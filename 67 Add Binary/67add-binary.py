class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        i, j = n - 1, m - 1
        ans, carry = [], 0

        while i >= 0 or j >= 0:
            an = int(a[i]) if i >= 0 else 0
            bn = int(b[j]) if j >= 0 else 0
            cn = an + bn + carry

            if cn in [0, 2]:
                ans.append('0')
            else:
                ans.append('1')
            
            carry = 1 if cn > 1 else 0
            i, j = i - 1, j - 1
        
        if carry:
            ans.append('1')

        ans.reverse()
        return ''.join(ans)