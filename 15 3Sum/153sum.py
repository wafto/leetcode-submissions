class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1

                    while j < n and nums[j - 1] == nums[j]:
                        j+= 1

                    while k + 1 < n - 1 and nums[k + 1] == nums[k]:
                        k -= 1          
    
        return ans
