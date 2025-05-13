class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {} # num: index

        for i, num in enumerate(nums):
            if num in hashmap and i - hashmap[num] <= k:
                return True
            hashmap[num] = i

        return False 
