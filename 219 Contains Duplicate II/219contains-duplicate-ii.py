class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}

        for i, num in enumerate(nums):
            if num in mapping and i - mapping[num] <= k:
                return True

            mapping[num] = i

        return False