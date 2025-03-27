class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominant = -1
        
        count = 0
        for num in nums:
            if count == 0:
                dominant = num
            count += 1 if num == dominant else -1

        n = len(nums)
        left_count = 0
        right_count = nums.count(dominant)

        for i in range(n):
            if nums[i] == dominant:
                left_count += 1
                right_count -= 1

            left_size = i + 1
            right_size = n - i - 1

            if (left_count << 1) > left_size and (right_count << 1) > right_size:
                return i

        return -1 