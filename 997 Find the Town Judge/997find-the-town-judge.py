class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        civilians = set()
        rank = defaultdict(int)

        if n == 1 and not trust:
            return 1

        for a, b in trust:
            civilians.add(a)
            rank[b] += 1

        if len(civilians) != n - 1:
            return -1

        judge = -1

        for person, count in rank.items():
            if count == n - 1:
                judge = person
                break

        return judge
        