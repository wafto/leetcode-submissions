class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtracking(i: int, curr: List[int]) -> None:
            if len(curr) >= k:
                ans.append(curr.copy())
                return

            for num in range(i, n + 1):
                curr.append(num)
                backtracking(num + 1, curr)
                curr.pop()

        backtracking(1, [])
        return ans


            
            
