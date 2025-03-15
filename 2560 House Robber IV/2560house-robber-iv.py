class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n, left, right = len(nums), min(nums), max(nums)

        def theftable(cap: int) -> bool:
            i, count = 0, 0
            while i < n:
                if nums[i] <= cap:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == k:
                    break
            return count == k
                
        while left <= right:
            mid = (right + left) // 2

            if theftable(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

