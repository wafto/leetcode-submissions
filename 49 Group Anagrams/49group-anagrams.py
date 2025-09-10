class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        def freq(word: str):
            freq = [0] * 26
            for c in word:
                freq[ord('a') - ord(c)] += 1
            return tuple(freq)

        for word in strs:
            hashmap[freq(word)].append(word)

        return list(hashmap.values())
