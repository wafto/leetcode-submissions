class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            num = numbers[left] + numbers[right]
            if num == target:
                return [left + 1, right + 1]
            if num < target:
                left += 1
            else:
                right -= 1

        return []