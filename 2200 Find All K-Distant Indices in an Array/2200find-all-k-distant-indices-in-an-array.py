class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n):
            if nums[i] == key:
                start = max(0 if not ans else ans[-1] + 1, i - k)
                end = min(n - 1, i + k)
                for i in range(start, end + 1):
                    ans.append(i)

        return ans