class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]

        for i in range(1, rowIndex + 1):
            nxt = [1] * (i + 1)
            for c in range(1, len(nxt) - 1):
                nxt[c] = ans[c - 1] + ans[c]
            ans = nxt

        return ans

