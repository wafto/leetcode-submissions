class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        combs = []

        def backtracking(i: int, curr: List[int], total: int) -> None:
            if i >= len(nums) and len(curr) == k and total == n:
                combs.append(curr.copy())
                return
            
            if i >= len(nums):
                return

            if total + nums[i] <= n:
                curr.append(nums[i])
                backtracking(i + 1, curr, total + nums[i])
                curr.pop()

            backtracking(i + 1, curr, total)

        backtracking(0, [], 0)
        return combs



            
