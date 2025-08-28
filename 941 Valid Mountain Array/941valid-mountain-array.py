class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, n = 1, len(arr)

        if n < 3:
            return False

        while i < n and arr[i - 1] < arr[i]:
            i += 1

        if i == 0 or i == n or arr[i - 1] == arr[i]:
            return False

        while i < n and arr[i - 1] > arr[i]:
            i += 1

        if i != n:
            return False

        return True