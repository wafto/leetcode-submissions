class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, ans = len(nums), 0

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 0 if nums[i + 1] else 1
                nums[i + 2] = 0 if nums[i + 2] else 1
                ans += 1

        return -1 if nums[-1] == 0 or nums[-2] == 0 else ans


            
        
            
    