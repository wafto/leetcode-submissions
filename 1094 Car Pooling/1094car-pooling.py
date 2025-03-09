class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        destinations = max(trip[2] for trip in trips)
        data = [0] * (destinations + 1)

        for (passengers, src, dst) in trips:
            data[src] += passengers
            data[dst] -= passengers

        prefix = 0
        
        for i in range(len(data)):
            prefix += data[i]
            if prefix > capacity:
                return False

        return True