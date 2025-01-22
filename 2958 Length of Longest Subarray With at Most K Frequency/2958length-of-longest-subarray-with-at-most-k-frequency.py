class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, longest = 0, 0
        frequency = defaultdict(int)

        for right in range(len(nums)):
            curr = nums[right]
            frequency[curr] += 1

            while frequency[curr] > k:
                frequency[nums[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
