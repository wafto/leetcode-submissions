class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = (10 ** 9) + 7
        ps, even_cnt, odd_cnt, ans = 0, 0, 0, 0

        for num in arr:
            ps += num

            if ps & 1:
                ans = (ans + 1 + even_cnt) % MOD
                odd_cnt += 1
            else:
                ans = (ans + odd_cnt) % MOD
                even_cnt += 1

        return ans