class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        prevs = set()
        
        for j in range(len(arr)):
            if arr[j] << 1 in prevs or (arr[j] & 1 == 0 and arr[j] >> 1 in prevs):
                return True
            prevs.add(arr[j])
                
        return False