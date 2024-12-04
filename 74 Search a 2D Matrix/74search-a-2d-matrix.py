class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        plain = matrix[0][:]

        for i in range(1, len(matrix)):
            plain.extend(matrix[i])

        left = 0
        right = len(plain) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if plain[middle] == target:
                return True

            if target < plain[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return False