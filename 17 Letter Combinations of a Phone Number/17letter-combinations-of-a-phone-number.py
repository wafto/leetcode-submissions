class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n, ans = len(digits), []
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

        if n == 0:
            return []

        def backtracking(i: int, curr: List[str]) -> None:
            if len(curr) == n:
                ans.append(''.join(curr))
                return

            for char in mapping[digits[i]]:
                curr.append(char)
                backtracking(i + 1, curr) 
                curr.pop()

        backtracking(0, [])
        return ans        
