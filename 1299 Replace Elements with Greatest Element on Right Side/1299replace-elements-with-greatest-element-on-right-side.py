class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        
        if size == 0: return []
        
        if size == 1: return [-1]
        
        greatest = -1
        
        for i in range(size - 1, -1, -1):
            tmp = arr[i]
            arr[i] = greatest
            greatest = max(greatest, tmp)
            
        return arr
            
            