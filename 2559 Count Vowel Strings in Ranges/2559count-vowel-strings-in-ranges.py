class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        output = [0] * len(queries)
        ps = [0] * len(words)

        acc = 0
        for i in range(len(words)):
            acc += 1 if words[i][0] in vowels and words[i][-1] in vowels else 0
            ps[i] = acc

        for i in range(len(queries)):
            l, r = queries[i]
            output[i] = ps[r] - (ps[l - 1] if l > 0 else 0)

        return output
