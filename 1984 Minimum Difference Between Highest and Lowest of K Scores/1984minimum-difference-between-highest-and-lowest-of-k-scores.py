class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        scores = sorted(nums)
        left, mindiff = 0, float(inf)

        for right in range(k - 1, len(scores)):
            mindiff = min(mindiff, scores[right] - scores[left])
            left += 1

        return mindiff




        