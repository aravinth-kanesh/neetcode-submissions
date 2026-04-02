class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if s == t:
            return 0

        left = 0
        for ch in s:
            if left < len(t) and ch == t[left]:
                left += 1

        if left == len(t):
            return 0

        return len(t[left:])