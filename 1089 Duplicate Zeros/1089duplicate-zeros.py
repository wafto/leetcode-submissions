class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        i = 0
        
        while i < size:
            if arr[i] == 0:
                j = size - 1
                while j > i:
                    arr[j] = arr[j - 1]
                    j -= 1
                arr[j] = 0
                i += 2
            else:
                i += 1
        
            
                
            
        