class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def comb(i: index, cur: List[int], acc: int) -> None:
            if acc > target or i >= len(candidates):
                return
            if acc == target:
                output.append(cur.copy())
                return
            cur.append(candidates[i])
            comb(i, cur, acc + candidates[i])

            cur.pop()
            comb(i + 1, cur, acc)

        comb(0, [], 0)
        return output

