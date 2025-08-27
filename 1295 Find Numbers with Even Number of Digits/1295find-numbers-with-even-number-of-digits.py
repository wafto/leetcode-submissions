class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if len(str(num)) & 1 == 0:
                count += 1

        return count
        