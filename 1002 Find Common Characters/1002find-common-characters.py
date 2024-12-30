class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        output = list(words[0])

        for i in range(1, len(words)):
            mp = dict()
            for c in words[i]:
                mp[c] = 1 + mp.get(c, 0)
            curr = []
            while output:
                c = output.pop()
                if c in mp and mp[c] >= 1:
                    mp[c] -= 1
                    curr.append(c)
            output = curr

        return output
            
