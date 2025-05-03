class Solution:
    def rob(self, nums: List[int]) -> int:
        robs = [0, 0]

        for num in nums:
            tmp = robs[1]
            robs[1] = max(num + robs[0], robs[1])
            robs[0] = tmp

        return robs[1]