class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    acc = nums[i] + nums[j] + nums[left] + nums[right]

                    if acc == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left, right = left + 1, right - 1

                        while left < right and nums[left - 1] == nums[left]:
                            left += 1

                        while left < right and nums[right + 1] == nums[right]:
                            right -= 1

                    elif acc < target:
                        left += 1
                    else:
                        right -= 1

        return ans