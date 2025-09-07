class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n, ans = len(candidates), []

        def backtracking(i: int, curr: List[int], acc: int) -> None:
            if acc == target:
                ans.append(curr.copy())
                return

            for j in range(i, n):
                total = candidates[j] + acc
                
                if total > target:
                    continue
                
                curr.append(candidates[j])
                backtracking(j, curr, total)
                curr.pop()


        backtracking(0, [], 0)
        return ans

