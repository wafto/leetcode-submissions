class Solution:
    def rob(self, nums: List[int]) -> int:
        robs = [0, 0]
        for n in nums:
            tmp = max(robs[0] + n, robs[1])
            robs[0] = robs[1]
            robs[1] = tmp
        return robs[1]