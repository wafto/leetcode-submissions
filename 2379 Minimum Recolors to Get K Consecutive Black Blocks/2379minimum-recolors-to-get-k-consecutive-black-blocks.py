class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, minimum, W = 0, len(blocks) + 1, 0

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                W += 1
            
            if right - left + 1 < k:
                continue

            while right - left + 1 > k:
                if blocks[left] == 'W':
                    W -= 1
                left += 1

            minimum = min(minimum, W)

        return minimum

