class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(curr: List[int], i: int, acc: int) -> None:
            if acc == target:
                combinations.append(curr.copy())
                return

            for j in range(i, len(candidates)):
                num = candidates[j]
                if acc + num > target:
                    continue
                curr.append(num)
                backtracking(curr, j, acc + num)
                curr.pop()

        backtracking([], 0, 0)
        return combinations
