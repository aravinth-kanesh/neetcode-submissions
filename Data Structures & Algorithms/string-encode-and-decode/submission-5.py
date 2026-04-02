class Solution:
    def encode(self, strs: List[str]) -> str:
        # intialise the encoded string
        encoded = ""
        for s in strs:
            # get length of each string and add delimiter
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        # initialise the decoded list of strings
        decoded = []
        i = j = 0
        while i < len(s):
            while s[j].isdigit():
                j += 1
            # length of word may be over one digit long
            length = int(s[i : j])
            word = s[j + 1 : j + 1 + length]
            # add decoded word to array
            decoded.append(word)
            # update pointers
            i = j + 1 + length
            j = i
        return decoded
        
