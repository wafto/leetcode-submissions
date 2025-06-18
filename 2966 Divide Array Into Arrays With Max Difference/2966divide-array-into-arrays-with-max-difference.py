class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(0, len(nums), 3):
            triplet = nums[i: i + 3]
            
            if triplet[2] - triplet[0] > k:
                return []

            ans.append(triplet)

        return ans
