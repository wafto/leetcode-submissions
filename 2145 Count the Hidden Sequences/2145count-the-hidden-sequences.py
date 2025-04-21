class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr, maximal, minimal = 0, 0, 0

        for num in differences:
            curr += num
            maximal = max(maximal, curr)
            minimal = min(minimal, curr)

        return max(0, upper - lower - maximal + minimal + 1)