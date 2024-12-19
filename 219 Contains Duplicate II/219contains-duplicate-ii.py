class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = dict()

        for index, value in enumerate(nums):
            if value in mapping and index - mapping[value] <= k:
                return True
            mapping[value] = index

        return False
