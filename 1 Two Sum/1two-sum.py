class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # diff: index O(n), O(n)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
