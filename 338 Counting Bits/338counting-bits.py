class Solution:
    def countBits(self, n: int) -> List[int]:
        weights = [0] * (n + 1)

        for i in range(1, n + 1):
            weights[i] = weights[i >> 1] + (i & 1)

        return weights
