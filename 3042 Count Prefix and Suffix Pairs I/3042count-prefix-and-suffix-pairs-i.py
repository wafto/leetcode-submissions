class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        output = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                wi, wj = words[i], words[j]
                if len(wi) <= len(wj) and wj.startswith(wi) and wj.endswith(wi):
                    output += 1

        return output