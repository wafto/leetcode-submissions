class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []

        def backtracking(i: int, curr: List[int]) -> None:
            if i >= len(nums):
                sets.append(curr.copy())
                return

            # Decide not to include nums[i]
            backtracking(i + 1, curr)

            # Decide to include nums[i]
            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()

        backtracking(0, [])
        return sets