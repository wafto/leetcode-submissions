class Solution:
    def countElements(self, arr: List[int]) -> int:
        hs = set(arr)
        ans = 0
        
        for n in arr:
            if n + 1 in hs:
                ans += 1
                
        return ans
        