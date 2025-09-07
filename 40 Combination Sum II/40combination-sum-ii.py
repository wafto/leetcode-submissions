class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, n = [], len(candidates)

        candidates.sort()

        def backtracking(i: int, curr: List[int], acc: int) -> None:
            if acc == target:
                ans.append(curr.copy())
                return

            for j in range(i, n):
                total = acc + candidates[j]
                
                if total > target:
                    continue
                
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                
                curr.append(candidates[j])
                backtracking(j + 1, curr, total)
                curr.pop()

        backtracking(0, [], 0)

        return ans