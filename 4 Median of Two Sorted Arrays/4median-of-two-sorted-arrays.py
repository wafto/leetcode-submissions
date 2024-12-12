class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        mid = (total // 2) + 1

        k = 0
        output = []
        while nums1 or nums2:
            n = None
            if k >= mid:
                break
            if nums1 and not nums2:
                n = nums1.pop(0)
            elif nums2 and not nums1:
                n = nums2.pop(0)
            elif nums1[0] < nums2[0]:
                n = nums1.pop(0)
            else:
                n = nums2.pop(0)
            output.append(n)
            k += 1

        osize = len(output)

        if total == 1:
            return output[0]
        if total % 2 == 0:
            return float(output[osize - 1] + output[osize - 2]) / 2
        else:
            return float(output[osize - 1])
        

                


