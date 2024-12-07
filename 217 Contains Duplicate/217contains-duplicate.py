class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        encounters = set()
        for n in nums:
            if n in encounters:
                return True
            encounters.add(n)
        return False