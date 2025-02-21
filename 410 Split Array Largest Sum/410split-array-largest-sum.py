class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def to_chunks(threshold: int) -> int:
            curr = 0
            chunks = 0
            for num in nums:
                if curr + num <= threshold:
                    curr += num
                else:
                    curr = num
                    chunks += 1
            return chunks + 1

        ans = 0
        left, right = max(nums), sum(nums)

        while left <= right:
            mid = (right + left) // 2

            if to_chunks(mid) <= k:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans
            
