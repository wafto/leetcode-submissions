class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashmap = {}
        ans = len(cards) + 1

        for i, card in enumerate(cards):
            if card in hashmap:
                ans = min(ans, i - hashmap[card] + 1)
            hashmap[card] = i

        return -1 if ans > len(cards) else ans

             