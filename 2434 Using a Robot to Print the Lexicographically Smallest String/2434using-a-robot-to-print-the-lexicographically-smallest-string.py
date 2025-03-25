class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        seq, curr = 'abcdefghijklmnopqrstuvwxyz', 0
        t, p = [], []

        for ch in s:
            cnt[ch] -= 1
            t.append(ch)

            while curr < len(seq) - 1 and cnt[seq[curr]] == 0:
                curr += 1

            while t and t[-1] <= seq[curr]:
                p.append(t.pop())

        return ''.join(p)
            

