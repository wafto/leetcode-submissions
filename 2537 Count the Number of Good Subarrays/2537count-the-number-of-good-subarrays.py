class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        n, left, pairs, ans = len(nums), 0, 0, 0

        for right in range(n):
            pairs += counter[nums[right]]
            counter[nums[right]] += 1

            while pairs >= k:
                ans += n - right
                counter[nums[left]] -= 1
                pairs -= counter[nums[left]]
                left += 1

        return ans

