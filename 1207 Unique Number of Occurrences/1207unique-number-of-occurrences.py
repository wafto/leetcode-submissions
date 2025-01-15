class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)

        for n in arr:
            counts[n] += 1

        occ = set()

        for cnt in counts.values():
            if cnt in occ:
                return False
            occ.add(cnt)

        return True
