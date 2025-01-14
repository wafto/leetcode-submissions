class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = [False] * len(candies)
        maxKid = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxKid:
                output[i] = True

        return output