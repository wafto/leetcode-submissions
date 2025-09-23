class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {i: [] for i in range(n)}

        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))
            
        heap = [(-1.0, start_node)] # (probability, node)
        probabilities = {} # node -> probability

        while heap:
            prob, node = heappop(heap)

            if node in probabilities:
                continue

            probabilities[node] = -prob

            if end_node == node:
                return probabilities[end_node]

            for nnode, nprob in graph[node]:
                if nnode in probabilities:
                    continue
                nprob *= prob
                heappush(heap, (nprob, nnode))

        return 0.0