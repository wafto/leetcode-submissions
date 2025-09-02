class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n, subs = len(nums), []

        def backtracking(i: int, curr: List[int]) -> None:
            if i >= n:
                subs.append(curr.copy())
                return

            # incluir nums[i]
            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()

            # no incluir 
            backtracking(i + 1, curr)

        backtracking(0, [])
        return subs



