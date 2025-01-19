class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l, r, w = 0, 0, list(word)

        while r < len(w) and w[r] != ch:
            r += 1

        if r == len(w):
            return word

        while l < r:
            w[l], w[r] = w[r], w[l]
            l += 1
            r -= 1
        
        return ''.join(w)