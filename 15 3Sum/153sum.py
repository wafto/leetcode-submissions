class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            j, k = i + 1, n - 1

            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            while j < k:
                acc = nums[i] + nums[j] + nums[k]

                if acc == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1

                    while j < k and nums[j - 1] == nums[j]:
                        j += 1

                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1

                elif acc > 0:
                    k -= 1
                else:
                    j += 1

        return ans
