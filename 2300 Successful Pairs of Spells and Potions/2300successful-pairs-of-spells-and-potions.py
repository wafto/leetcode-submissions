class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        def binary_search(data: List[int], target: int) -> int:
            left, right = 0, len(data)

            while left < right:
                mid = (right + left) // 2
                if data[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            
            return left

        ans = []
        potions.sort()

        for spell in spells:
            i = binary_search(potions, success / spell)
            ans.append(len(potions) - i)

        return ans

