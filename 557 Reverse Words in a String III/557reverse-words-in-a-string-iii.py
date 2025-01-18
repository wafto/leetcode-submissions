class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverse(word: str) -> str:
            W = list(word)
            L, R = 0, len(W) - 1
            while L < R:
                W[L], W[R] = W[R], W[L]
                L += 1
                R -= 1
            return ''.join(W)

        words = s.split()
        
        for i in range(len(words)):
            words[i] = reverse(words[i])

        return ' '.join(words)


