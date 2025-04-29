class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(num: int, curr: List[int]) -> None:
            if len(curr) == k:
                res.append(curr.copy())
                return

            for num2 in range(num, n + 1):
                curr.append(num2)
                backtracking(num2 + 1, curr)
                curr.pop()

        backtracking(1, [])
        return res
