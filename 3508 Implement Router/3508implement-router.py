class Router:

    def __init__(self, memoryLimit: int):
        self.queue = deque()
        self.mem = memoryLimit
        self.used = set()
        self.l = 0
        self.dest = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        
        if packet in self.used:
            return False
        
        if self.l >= self.mem:
            prev = self.queue.popleft()
            self.used.remove(prev)
            self.dest[prev[1]].pop(0)
            self.l -= 1

        self.queue.append(packet)
        self.used.add(packet)
        self.dest[destination].append(timestamp)
        self.l += 1
        return True
        
    def forwardPacket(self) -> List[int]:
        if self.l == 0:
            return []
        self.l -= 1
        packet = self.queue.popleft()
        self.used.remove(packet)
        self.dest[packet[1]].pop(0)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        a = self.dest[destination]
        return bisect.bisect_right(a, endTime) - bisect.bisect_left(a, startTime)
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)