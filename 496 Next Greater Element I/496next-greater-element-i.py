class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}

        for num in nums2:
            while stack and stack[-1] < num:
                n = stack.pop()
                mapping[n] = num
            stack.append(num)

        return list(map(lambda n: mapping.get(n, -1), nums1))