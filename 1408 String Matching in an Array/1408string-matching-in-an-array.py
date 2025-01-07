class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set()

        while words:
            curr = words.pop()
            for word in words:
                if len(word) <= len(curr) and word in curr:
                    output.add(word)
                    continue

                if len(word) >= len(curr) and curr in word:
                    output.add(curr)
                
        return list(output)