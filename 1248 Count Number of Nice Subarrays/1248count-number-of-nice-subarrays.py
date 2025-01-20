class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans, ps = 0, 0
        hashmap = {0: 1}

        for n in nums:
            ps += n & 1
            diff = ps - k
            if diff in hashmap:
                ans += hashmap[diff]
            hashmap[ps] = 1 + hashmap.get(ps, 0)

        return ans