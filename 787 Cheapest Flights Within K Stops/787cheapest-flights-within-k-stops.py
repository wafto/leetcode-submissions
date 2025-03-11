class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, 0, src)] # price, stops, city
        visited = {}

        while heap:
            price, stops, city = heapq.heappop(heap)

            if stops > k + 1:
                continue

            if city == dst:
                return price

            if city in visited and visited[city] == stops:
                continue

            visited[city] = stops

            for neighbor, price2 in graph[city]:
                if neighbor not in visited or visited[neighbor] > stops:
                    heapq.heappush(heap, (price + price2, stops + 1, neighbor))

        return -1
                
