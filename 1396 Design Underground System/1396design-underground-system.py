class UndergroundSystem:
    def __init__(self):
        self.checkIns = dict()
        self.averages = defaultdict(lambda: [0, 0])   

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkIns[id]
        route = (start, stationName)
        self.averages[route][0] += t - time
        self.averages[route][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, count = self.averages[(startStation, endStation)]
        return time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)