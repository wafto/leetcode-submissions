class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, len(nums)
        
        while i < k:
            if nums[i] == val:
                j = i
                while j < k - 1:
                    nums[j] = nums[j + 1]
                    j += 1
                k -= 1
            else:
                i += 1
                
        return k