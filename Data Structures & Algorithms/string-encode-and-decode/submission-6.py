class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = j = 0
        while i < len(s):
            while j < len(s) and s[j].isdigit():
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)
            i = j + 1 + length
            j = i
        return decoded