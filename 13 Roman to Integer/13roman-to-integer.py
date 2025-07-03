class Solution:
    def romanToInt(self, s: str) -> int:
        ans, n = 0, len(s)
        hashmap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        index = 0
        while index < n:
            if index + 1 < n and hashmap[s[index]] < hashmap[s[index + 1]]:
                ans += hashmap[s[index + 1]] - hashmap[s[index]]
                index += 2
            else:
                ans += hashmap[s[index]]
                index += 1

        return ans


