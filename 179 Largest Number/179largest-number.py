class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        nums.sort(key=lambda s: s * 10, reverse=True)
        
        # if the largest is '0' we assume that everything else is '0'
        if nums[0] == '0':
            return '0'

        return ''.join(nums)