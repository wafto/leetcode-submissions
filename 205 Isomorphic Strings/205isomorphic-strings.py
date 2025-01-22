class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ms, mt = {}, {}

        for cs, ct in zip(s, t):
            if ct in ms and ms[ct] != cs:
                return False
            if cs in mt and mt[cs] != ct:
                return False
            ms[ct] = cs
            mt[cs] = ct  

        return True
        