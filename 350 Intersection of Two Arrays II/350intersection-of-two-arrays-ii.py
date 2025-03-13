class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        intersection = []

        for num, cnt in cnt1.items():
            if num in cnt2:
                intersection.extend([num] * min(cnt1[num], cnt2[num]))

        return intersection
        