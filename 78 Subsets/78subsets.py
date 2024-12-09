class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []
        def sub(index):
            if index >= len(nums):
                output.append(subset.copy())
                return
            subset.append(nums[index])
            sub(index + 1)
            subset.pop()
            sub(index + 1)
        sub(0)
        return output
