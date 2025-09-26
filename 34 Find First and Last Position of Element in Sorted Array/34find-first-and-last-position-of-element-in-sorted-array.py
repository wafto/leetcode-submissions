class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def bs(left: bool) -> int:
            l, r = 0, n - 1
            ans = -1

            while l <= r:
                m = (r + l) // 2

                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    ans = m
                    if left:
                        r = m - 1
                    else:
                        l = m + 1

            return ans

        return [bs(True), bs(False)] 
                    
