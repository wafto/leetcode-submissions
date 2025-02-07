class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = defaultdict(int)
        colors, ans = defaultdict(int), []

        for i, color in queries:

            if balls[i] != 0:
                if colors[balls[i]] == 1:
                    del colors[balls[i]]
                else:
                    colors[balls[i]] -= 1

            balls[i] = color
            colors[color] += 1

            ans.append(len(colors))

        return ans

