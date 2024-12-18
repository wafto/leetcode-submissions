class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = dict()

        for word in strs:
            tmp = list(word)
            tmp.sort()
            tmp = ''.join(tmp)
            if tmp not in output:
                output[tmp] = []
            output[tmp].append(word)

        return list(output.values())
