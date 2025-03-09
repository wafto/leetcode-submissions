class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        left, ans, n = 0, 0, len(s)
        freq = defaultdict(int)

        for right in range(n):
            freq[s[right]] += 1

            if right - left + 1 < k:
                continue

            while right - left + 1 > k:
                if freq[s[left]] == 1:
                    del freq[s[left]]
                else:
                    freq[s[left]] -= 1
                left += 1

            if len(freq) == k:
                ans += 1

        return ans

            
        

