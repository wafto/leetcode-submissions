class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtracking(curr: List[int], num: int) -> None:
            if len(curr) == k:
                combinations.append(curr.copy())
                return

            for x in range(num, n + 1):
                curr.append(x)
                backtracking(curr, x + 1)
                curr.pop()

        backtracking([], 1)
        return combinations