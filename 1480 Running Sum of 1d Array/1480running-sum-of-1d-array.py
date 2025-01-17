class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        acc = 0
        for i in range(n):
            acc += nums[i]
            ans[i] = acc
            
        return ans