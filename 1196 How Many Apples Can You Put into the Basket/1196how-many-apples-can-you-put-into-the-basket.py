class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        carry, i, apples = 5000, 0, 0

        while carry > 0 and i < len(weight):
            if weight[i] <= carry:
                carry -= weight[i]
                i, apples = i + 1, apples + 1
            else:
                break

        return apples
        