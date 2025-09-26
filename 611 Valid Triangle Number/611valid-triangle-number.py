class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Triangle: side1 + side2 > side 3

        nums.sort()
        ans, n = 0, len(nums)
    
        if n < 3:
            return 0

        for c in range(n - 1, 1, - 1):
            a, b = 0, c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    ans += b - a
                    b -= 1
                else:
                    a += 1

        return ans





            

