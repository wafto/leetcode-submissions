class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        ans = [i for i in range(1, n)]

        ans.append(n * (n - 1) // -2)

        return ans