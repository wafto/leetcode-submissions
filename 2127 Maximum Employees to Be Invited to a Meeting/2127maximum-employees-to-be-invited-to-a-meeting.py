class Solution:
    '''
    Revist link https://www.youtube.com/watch?v=aPBELJa-LM8
    this is a heavy hard problem
    '''
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        longest = 0
        visited = [False] * n
        length2cycles = []

        for i in range(n):
            if visited[i]:
                continue
            
            start, curr = i, i
            currSet = set()
            
            while not visited[curr]:
                visited[curr] = True
                currSet.add(curr)
                curr = favorite[curr]

            if curr in currSet:
                length = len(currSet)
                while start != curr:
                    length -= 1
                    start = favorite[start]
                
                longest = max(longest, length)
                
                if length == 2:
                    length2cycles.append([curr, favorite[curr]])
                
        inverted = defaultdict(list)
        for dst, src in enumerate(favorite):
            inverted[src].append(dst)

        def bfs(src, parent):
            q = deque([(src, 0)])
            mlength = 0
            while q:
                node, length = q.popleft()
                if node == parent:
                    continue
                mlength = max(mlength, length)
                for n in inverted[node]:
                    q.append((n, length + 1))
            return mlength

        chain = 0

        for n1, n2 in length2cycles:
            chain += bfs(n1, n2) + bfs(n2, n1) + 2

        return max(chain, longest)
        