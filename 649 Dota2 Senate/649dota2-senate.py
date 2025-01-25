class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()

        for i, s in enumerate(senate):
            if s == 'R':
                R.append(i)
            else:
                D.append(i)

        n = len(senate)

        while R and D:
            if R.popleft() < D.popleft():
                R.append(n)
            else:
                D.append(n)
            n += 1

        return 'Radiant' if not D else 'Dire'


