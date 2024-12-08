class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix = strs.pop(0)

        for word in strs[::-1]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
