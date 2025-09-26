class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        while left < right:
            mid = (right + left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left]
