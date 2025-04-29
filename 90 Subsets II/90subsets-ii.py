class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sets = []

        nums.sort()

        def backtracking(i: int, curr: List[int]) -> None:
            if i >= len(nums):
                sets.append(curr.copy())
                return

            # include
            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()

            # not include
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtracking(i + 1, curr)

        backtracking(0, [])
        return sets