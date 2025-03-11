class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, ans, n = 0, 0, len(s)
        freq = defaultdict(int)

        for right in range(n):
            freq[s[right]] += 1

            while len(freq) == 3:
                ans += n - right
                if freq[s[left]] == 1:
                    freq.pop(s[left])
                else:
                    freq[s[left]] -= 1
                left += 1

        return ans