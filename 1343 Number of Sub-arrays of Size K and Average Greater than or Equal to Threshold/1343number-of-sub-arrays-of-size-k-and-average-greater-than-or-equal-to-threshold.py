class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        ps = [0] * (n + 1)

        prev = 0
        for i in range(n):
            prev += arr[i]
            ps[i + 1] = prev

        left, ans = 0, 0
        for right in range(k, len(ps)):
            if (ps[right] - ps[left]) // k >= threshold:
                ans += 1
            left += 1

        return ans
