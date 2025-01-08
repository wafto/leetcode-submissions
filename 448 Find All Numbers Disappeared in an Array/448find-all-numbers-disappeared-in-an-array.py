class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        existing = set(nums)
        missing = []

        for n in range(1, len(nums) + 1):
            if n not in existing:
                missing.append(n)

        return missing
