class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(left: int, right: int, curr: List[str]) -> None:
            if len(curr) == n * 2:
                ans.append(''.join(curr))
                return

            if left < n:
                curr.append('(')
                backtracking(left + 1, right, curr)
                curr.pop()

            if left > right:
                curr.append(')')
                backtracking(left, right + 1, curr)
                curr.pop()

        backtracking(0, 0, [])
        return ans




