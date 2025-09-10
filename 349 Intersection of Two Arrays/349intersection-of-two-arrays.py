class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = set(nums2)
        answer = set()

        for num in nums1:
            if num in nums2:
                answer.add(num)
        
        return list(answer)
