class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        s = len(arr)
        
        if s < 3:
            return False
        
        i = 0
        while i < s - 1 and arr[i] < arr[i + 1]:
            i += 1
            
        if i == 0 or i == s - 1 or arr[i - 1] == arr[i]:
            return False
        
        while i < s - 1 and arr[i] > arr[i + 1]:
            i += 1
            
        if i != s - 1:
            return False
        
        return True
            
        
        
        
        