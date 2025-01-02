class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        i, j = 0, 0
        
        while i < m + n and j < n:
            if nums1[i] > nums2[j]:
                k = m + n - 1
                while k > i:
                    nums1[k] = nums1[k - 1]
                    k -= 1
                nums1[i] = nums2[j]
                j += 1
            i += 1
                
        k = m + j
                
        while k < m + n:
            nums1[k] = nums2[j]
            k += 1
            j += 1

            
            
        
        