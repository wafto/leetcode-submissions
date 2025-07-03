class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        while len(word) < k:
            curr = list(word)
            for i in range(len(curr)):
                curr[i] = 'a' if curr[i] == 'z' else chr(ord(curr[i]) + 1)
            word = word + ''.join(curr)

        return word[k - 1]