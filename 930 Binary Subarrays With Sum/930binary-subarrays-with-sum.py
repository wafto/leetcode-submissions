class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curr, subarrays = 0, 0
        ps = defaultdict(int)
        ps[0] = 1

        for n in nums:
            curr += n
            subarrays += ps[curr - goal]            
            ps[curr] += 1

        return subarrays