class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.insert(0, 0)
        spaces.append(len(s))
        output = ""

        for i in range(len(spaces) - 1):
            start = spaces[i]
            end = spaces[i + 1]
            output += s[start:end] + " "

        return output[:-1]
