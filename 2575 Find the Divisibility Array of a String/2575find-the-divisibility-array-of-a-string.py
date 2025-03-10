class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        curr, ans = 0, []

        for digit in word:
            curr = (curr * 10 + int(digit)) % m
            ans.append(1 if curr == 0 else 0)

        return ans