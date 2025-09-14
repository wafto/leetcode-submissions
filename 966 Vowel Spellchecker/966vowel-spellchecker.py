class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans = []

        exacts = set(wordlist)
        lowers = {}
        devowels = {}

        def devowelize(word: str) -> str:
            return ''.join(['*' if c in 'aeiou' else c for c in word])

        for w in wordlist:
            lower = w.lower()
            lowers.setdefault(lower, w)
            devowels.setdefault(devowelize(lower), w)

        for q in queries:
            if q in exacts:
                ans.append(q)
                continue

            lower = q.lower()
            
            if lower in lowers:
                ans.append(lowers[lower])
                continue

            devowel = devowelize(lower)

            if devowel in devowels:
                ans.append(devowels[devowel])
                continue

            ans.append('')

        return ans
            
