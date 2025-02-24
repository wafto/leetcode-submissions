class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def backtracking(curr: List[str], i: int) -> None:
            if len(curr) == len(digits):
                if curr:
                    combinations.append(''.join(curr))
                return

            for j in range(i, len(digits)):
                for c in mapping[digits[j]]:
                    curr.append(c)
                    backtracking(curr, j + 1)
                    curr.pop()

        backtracking([], 0)
        return combinations

            

            
