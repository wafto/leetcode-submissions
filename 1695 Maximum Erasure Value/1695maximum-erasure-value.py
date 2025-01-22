class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, score, curr = 0, 0, 0
        counter = defaultdict(int)

        for right in range(len(nums)):
            curr += nums[right]
            counter[nums[right]] += 1

            while counter[nums[right]] > 1:
                curr -= nums[left]
                counter[nums[left]] -= 1
                left += 1

            score = max(score, curr)

        return score



