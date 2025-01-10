class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxfreq = [0] * 26
        output = []

        for word in words2:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - 97] += 1
            for i in range(26):
                maxfreq[i] = max(maxfreq[i], freq[i])

        for word in words1:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - 97] += 1
            universal = True
            for i in range(26):
                if maxfreq[i] > freq[i]:
                    universal = False
                    break
            if universal:
                output.append(word)
            
        return output


