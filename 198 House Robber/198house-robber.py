class Solution:
    def rob(self, nums: List[int]) -> int:
        robs = [0, 0]

        for num in nums:
            tmp = max(robs[0] + num, robs[1])
            robs[0] = robs[1]
            robs[1] = tmp

        return robs[1]

        
