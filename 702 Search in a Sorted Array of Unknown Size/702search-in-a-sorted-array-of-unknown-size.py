# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        outbound = (2 ** 31) - 1
        left, right = 0, (target - reader.get(0)) * 2

        while left <= right:
            mid = (right + left) // 2
            val = reader.get(mid)

            if val == outbound:
                right = mid - 1
            elif val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return mid

        return -1


