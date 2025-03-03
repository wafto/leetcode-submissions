class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        i, j, k = 0, n - 1, n -1
        ans = [pivot] * n

        for num in nums:
            if num < pivot:
                ans[i] = num
                i += 1
            elif num > pivot:
                ans[j] = num
                j -= 1

        j += 1
        while j < k:
            ans[j], ans[k] = ans[k], ans[j]
            j, k = j + 1, k - 1

        return ans
        

            


            