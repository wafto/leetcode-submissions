class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []

        def backtracking(curr: List[str], left_cnt, right_cnt) -> None:
            if len(curr) == 2 * n:
                combinations.append(''.join(curr))
                return
            
            if left_cnt < n:
                curr.append('(')
                backtracking(curr, left_cnt + 1, right_cnt)
                curr.pop()
            if right_cnt < left_cnt:
                curr.append(')')
                backtracking(curr, left_cnt, right_cnt + 1)
                curr.pop()

        backtracking([], 0, 0)
        return combinations       