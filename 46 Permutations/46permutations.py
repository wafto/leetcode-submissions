class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)

        def backtracking(curr: List[int]) -> None:
            if len(curr) == n:
                ans.append(curr.copy())
                return

            for num in nums:
                if num in curr:
                    continue
                curr.append(num)
                backtracking(curr)
                curr.pop()

        backtracking([])
        return ans