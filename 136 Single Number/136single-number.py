class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        st = set()

        for n in nums:
            if n in st:
                st.remove(n)
            else:
                st.add(n)

        return st.pop()