class Solution:
    def compress(self, chars: List[str]) -> int:
        size = len(chars)
        if size == 1:
            return 1

        comp = ''
        
        left = 0
        for right in range(size):
            if chars[right] != chars[left]:
                ch, cnt = chars[left], right - left
                comp += ch + (str(cnt) if cnt > 1 else '')
                left = right
            if right == size - 1:
                ch, cnt = chars[left], right - left + 1
                comp += ch + (str(cnt) if cnt > 1 else '')

        for i in range(len(comp)):
            chars[i] = comp[i]

        return len(comp)