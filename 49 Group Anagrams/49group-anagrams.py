class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def frequency(word: str) -> Tuple[int]:
            ord_a = ord('a')
            ans = [0] * 26
            for c in word:
                ans[ord(c) - ord_a] += 1
            return tuple(ans)

        groups = defaultdict(list)

        for word in strs:
            groups[frequency(word)].append(word)

        return list(groups.values())
