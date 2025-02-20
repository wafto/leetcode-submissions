class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def divisor_sum(d: int) -> int:
            total = 0
            for num in nums:
                total += ceil(num / d)
            return total

        left, right = 1, max(nums)

        while left <= right:
            mid = (right + left) // 2
            if divisor_sum(mid) <= threshold:
                right = mid - 1
            else:
                left = mid + 1

        return left