class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans, left = 0, 0
        types = defaultdict(int)

        for right in range(len(fruits)):
            types[fruits[right]] += 1
            
            while len(types) > 2:
                types[fruits[left]] -= 1
                if types[fruits[left]] == 0:
                    del types[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans