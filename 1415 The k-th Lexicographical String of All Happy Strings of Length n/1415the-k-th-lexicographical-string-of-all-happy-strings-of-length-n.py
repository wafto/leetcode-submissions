class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        generable = 3 * 2 ** (n - 1)
        left, right = 1, generable
        choices = 'abc'
        ans = []

        for i in range(n):
            curr = left
            partition = (right - left + 1) // len(choices)

            for c in choices:
                if k in range(curr, curr + partition):
                    ans.append(c)
                    left = curr
                    right = curr + partition - 1
                    choices = 'abc'.replace(c, '')
                    break
                curr += partition

        return ''.join(ans)


