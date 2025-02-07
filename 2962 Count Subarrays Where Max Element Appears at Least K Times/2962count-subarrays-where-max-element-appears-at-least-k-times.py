class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, cnt, num = 0, 0, max(nums)
        ans = 0

        for right in range(len(nums)):
            if nums[right] == num:
                cnt += 1
            
            while cnt >= k:
                if nums[left] == num:
                    cnt -= 1
                left += 1

            ans += left

        return ans