class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maxfreq = max(counter.values())
        ans = 0

        for x in counter.values():
            ans += x if x == maxfreq else 0

        return ans
        