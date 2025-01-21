class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0

        for num, count in counter.items():
            ans += num if count == 1 else 0

        return ans 

