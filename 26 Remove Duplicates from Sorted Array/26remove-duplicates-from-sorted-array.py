class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = len(nums)
        index = 1
        
        if s <= 1:
            return s
        
        for i in range(1, s):
            if nums[index - 1] != nums[i]:
                nums[index] = nums[i]
                index += 1
                
        return index
        