class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations, n = [], len(candidates)

        def backtrack(curr: List[int], i: int, total: int) -> None:
            if total == target:
                combinations.append(curr.copy())
                return

            if i >= n or total > target:
                return

            num = candidates[i]

            # use the same num
            curr.append(num)
            backtrack(curr, i, total + num)
            curr.pop()

            # not use the same num 
            backtrack(curr, i + 1, total)

        backtrack([], 0, 0)
        return combinations