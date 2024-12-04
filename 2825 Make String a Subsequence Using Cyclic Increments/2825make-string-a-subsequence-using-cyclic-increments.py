class Solution:
    def buildAlphabetDictionary(self) -> dict:
        dictionary = {}
        alphabet = string.ascii_letters[:26]

        for i in range(25):
            dictionary[alphabet[i]] = alphabet[i + 1]
        dictionary[alphabet[25]] = alphabet[0]

        return dictionary

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False

        dictionary = self.buildAlphabetDictionary()
        i = 0
        j = 0

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or dictionary[str1[i]] == str2[j]:
                j += 1
            i += 1
            
        return j == len(str2)
