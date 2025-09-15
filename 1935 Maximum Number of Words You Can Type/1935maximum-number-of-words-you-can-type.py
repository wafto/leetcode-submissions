class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans, bad = 0, set(brokenLetters)
        n, i = len(text), 0

        while i < n:
            broke = False
            
            while i < n and text[i] != ' ':
                if not broke and text[i] in bad:
                    broke = True
                i += 1
            
            ans += 0 if broke else 1
            i += 1

        return ans

            
        

