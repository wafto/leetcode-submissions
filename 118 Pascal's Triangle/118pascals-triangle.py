class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for num in range(1, numRows):
            line = [1] * (num + 1)
            prev = ans[-1]
            for i in range(num - 1):
                line[i + 1] = prev[i] + prev[i + 1]
            ans.append(line)

        return ans
