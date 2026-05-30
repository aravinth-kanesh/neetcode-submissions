class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []

        for st in strs:
            res.append(f"{len(st)}#{st}")

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i = i + length
        
        return res
