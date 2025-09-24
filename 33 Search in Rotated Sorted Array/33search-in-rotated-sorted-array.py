class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        def bs(left: int, right: int) -> int:
            while left <= right:
                mid = (right + left) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1

        ans = bs(0, left - 1)

        return ans if ans != -1 else bs(left, n - 1)

