class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        size = len(s)
        L, U = [], []

        if size & 1 == 1:
            return False

        for i in range(size):
            if locked[i] == '0':
                U.append(i)
            elif s[i] == '(':
                L.append(i)
            else:
                if L: L.pop()
                elif U: U.pop()
                else: return False

        while U and L and U[-1] > L[-1]:
            U.pop()
            L.pop()

        if L:
            return False

        return True

        