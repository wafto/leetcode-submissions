class Codec:
    def encode(self, strs: List[str]) -> str:
        encoding = []
        
        for word in strs:
            encoding.append(word)
        
        return '@SEP@'.join(encoding)

            
    def decode(self, s: str) -> List[str]:
        ans = []

        for word in s.split('@SEP@'):
            ans.append(word)

        return ans
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))