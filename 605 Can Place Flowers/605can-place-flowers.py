class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)

        if n == 0:
            return True

        for i in range(size):
            if flowerbed[i] == 0 and ((i - 1 < 0) or flowerbed[i - 1] == 0) and ((i + 1 >= size) or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        return False
