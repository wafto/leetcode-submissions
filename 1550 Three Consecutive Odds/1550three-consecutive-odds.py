class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        left, right = 0, 1
        consecutive = 0

        while right < len(arr) and left < len(arr):
            if arr[left] % 2 == 1:
                consecutive += 1
                left += 1
            else:
                consecutive = 0
                left = right
                right += 1

            if consecutive >= 3:
                return True
        
        return False