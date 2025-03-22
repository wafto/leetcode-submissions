class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for row in range(1, numRows):
            curr = [1]
            for i in range(1, row):
                curr.append(ans[-1][i - 1] + ans[-1][i])
            curr.append(1)
            ans.append(curr)

        return ans
