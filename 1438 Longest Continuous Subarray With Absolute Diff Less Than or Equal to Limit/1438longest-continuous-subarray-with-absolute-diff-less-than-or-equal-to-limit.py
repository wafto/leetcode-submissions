class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc, dec = deque(), deque()
        left, ans = 0, 0

        for right in range(len(nums)):
            while inc and inc[-1] > nums[right]:
                inc.pop()
            
            while dec and dec[-1] < nums[right]:
                dec.pop()
            
            inc.append(nums[right])
            dec.append(nums[right])

            if abs(dec[0] - inc[0]) > limit:
                if inc[0] == nums[left]:
                    inc.popleft()
                if dec[0] == nums[left]:
                    dec.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans
                

