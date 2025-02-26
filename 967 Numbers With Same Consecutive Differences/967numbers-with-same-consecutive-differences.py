class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        combinations = []

        def backtracking(curr: List[int]) -> None:
            if len(curr) == n:
                combinations.append(int(''.join(map(str, curr))))
                return

            for num in range(10):
                if not curr:
                    if num != 0:
                        curr.append(num)
                        backtracking(curr)
                        curr.pop()
                elif abs(curr[-1] - num) == k:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()

        backtracking([])
        return combinations          
