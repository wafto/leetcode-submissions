class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size_haystack = len(haystack)
        size_needle = len(needle)
        
        if size_haystack < size_needle:
            return -1
        
        if size_haystack == size_needle:
            return 0 if haystack == needle else -1

        for i in range(0, size_haystack - size_needle + 1):
            substr = haystack[i:i + size_needle]
            if substr == needle:
                return i


        return -1
            