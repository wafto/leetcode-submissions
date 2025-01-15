class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        size = len(gain)
        ps = [0] * (size + 1)
        highest = 0

        for i in range(size):
            ps[i] = ps[i - 1] + gain[i]
            highest = max(highest, ps[i])

        return highest