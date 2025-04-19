class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()

        def binary_search(target: int) -> int:
            left, right = 0, n - 1
            count = 0

            while left < right:
                curr = nums[left] + nums[right]
                if curr < target:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
            
            return count

        return binary_search(upper + 1) - binary_search(lower) 

        