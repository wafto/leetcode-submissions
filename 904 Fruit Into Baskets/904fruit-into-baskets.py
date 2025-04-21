class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n, left, maximal = len(fruits), 0, 0
        hashmap = defaultdict(int)

        for right in range(n):
            hashmap[fruits[right]] += 1

            while len(hashmap) > 2:
                if hashmap[fruits[left]] == 1:
                    del hashmap[fruits[left]]
                else:
                    hashmap[fruits[left]] -= 1
                left += 1

            maximal = max(maximal, right - left + 1)

        return maximal
        

