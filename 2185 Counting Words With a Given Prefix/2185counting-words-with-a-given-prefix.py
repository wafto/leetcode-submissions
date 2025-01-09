class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        output = 0
        preflen = len(pref)

        for word in words:
            if len(word) >= preflen and word[:preflen] == pref:
                output += 1

        return output
