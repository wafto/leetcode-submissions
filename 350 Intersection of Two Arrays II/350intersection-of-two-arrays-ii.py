class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        answer = []

        for num, cnt in count1.items():
            if num in count2:
                answer.extend([num] * min(cnt, count2[num]))

        return answer
