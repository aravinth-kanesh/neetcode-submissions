class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        if not strs:
            return res

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        i = 0

        while i < len(s):
            length = ""
           
            while s[i] != "#":
                length += s[i]
                i += 1  

            i += 1  
            length = int(length)
            res.append(s[i : i + length])
            i += length
            
        return res

        return res