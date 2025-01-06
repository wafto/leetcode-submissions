class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)
        ps = [0] * size

        acc, count = 0, 0
        for i in range(size):
            ps[i] += acc
            count += 1 if boxes[i] == '1' else 0
            acc += count

        acc, count = 0, 0
        for i in range(size - 1, -1, -1):
            ps[i] += acc
            count += 1 if boxes[i] == '1' else 0
            acc += count

        return ps