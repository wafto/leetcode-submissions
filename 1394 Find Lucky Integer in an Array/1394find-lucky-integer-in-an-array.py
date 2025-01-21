class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        lucky = -1

        for num, freq in counter.items():
            if num == freq:
                lucky = max(lucky, num)

        return lucky
