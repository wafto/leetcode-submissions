class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted([(b[1], b[0]) for b in boxTypes], reverse=True)
        i, ans = 0, 0

        while truckSize > 0 and i < len(boxTypes):
            units, boxes = boxTypes[i]
            cap = min(truckSize, boxes)
            ans += cap * units
            truckSize -= cap
            i += 1

        return ans