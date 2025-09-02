class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        
        k = k % n

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        