class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i: int, curr: List[int]) -> None:
            if i >= n:
                res.append(curr.copy())
                return

            # skip
            dfs(i + 1, curr)

            # take nums[i]
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

        dfs(0, [])
        return res