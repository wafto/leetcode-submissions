class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                curr = nums[i] + nums[j] + nums[k]

                if abs(target - curr) < abs(target - best):
                    best = curr

                if curr < target:
                    j += 1
                elif curr > target:
                    k -= 1
                else:
                    return curr

        return best