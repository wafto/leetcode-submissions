class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spaces, size = 0, len(flowerbed)

        for i in range(size):
            if flowerbed[i] != 0:
                continue

            left = (i == 0) or (flowerbed[i - 1] == 0)
            right = (i == size - 1) or (flowerbed[i + 1] == 0)

            if left and right:
                flowerbed[i] = 1
                spaces += 1

        return spaces >= n



