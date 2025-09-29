class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}

        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                j = stack.pop()
                mapping[nums2[j]] = num
            stack.append(i)

        return [mapping.get(n, -1) for n in nums1]
            