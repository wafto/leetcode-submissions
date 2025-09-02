class Solution:
    def reverseWords(self, s: str) -> str:
        buffer, ans = [], []

        for c in s:
            if c != ' ':
                buffer.append(c)
            elif buffer:
                ans.append(''.join(buffer))
                buffer = []
            
        if buffer:
            ans.append(''.join(buffer))

        ans.reverse()

        return ' '.join(ans)


