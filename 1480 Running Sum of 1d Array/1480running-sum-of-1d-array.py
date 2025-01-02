class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            output[i] = count

        return output 