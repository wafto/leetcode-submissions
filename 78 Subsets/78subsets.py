class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtracking(curr: List[int], i: int) -> None:
            if i > len(nums):
                return

            subsets.append(curr.copy())

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtracking(curr, j + 1)
                curr.pop()    

        backtracking([], 0)
        return subsets
            