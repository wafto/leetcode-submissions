class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashset = set()

        for num in arr:
            if num * 2 in hashset:
                return True
            if num & 1 == 0 and num // 2 in hashset:
                return True
            hashset.add(num)

        return False

