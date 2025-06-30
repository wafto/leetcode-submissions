class Solution:
    def findLHS(self, nums: List[int]) -> int:
        longest = 0
        count = Counter(nums)

        for key in count:
            if key + 1 in count:
                longest = max(longest, count[key] + count[key + 1])
            
        return longest
