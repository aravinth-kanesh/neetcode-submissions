class Solution:
    def encode(self, strs: List[str]) -> str:
        # the issue is numbers can be part of a string
        # format - len, delimiter, string
        res = []

        for st in strs:
            length = len(st)
            res.append(f"{length}#{st}")
        
        print("".join(res))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            st = s[i:i + length]
            res.append(st)
            i = i + length

        return res


