class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []

        def backtracking(curr: List[int], acc: int, start: int) -> None:
            if acc == n and len(curr) == k:
                combinations.append(curr.copy())
                return

            if acc > n or len(curr) > k:
                return

            for num in range(start, 10):
                if acc + num > n:
                    continue
                curr.append(num)
                backtracking(curr, acc + num, num + 1)
                curr.pop()

        backtracking([], 0, 1)
        return combinations
        