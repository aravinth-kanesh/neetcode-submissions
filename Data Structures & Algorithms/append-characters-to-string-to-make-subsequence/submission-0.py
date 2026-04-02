class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        appends = 0

        # edge case
        if s == t:
            return appends

        left = 0

        for ch in s:
            if left < len(t) and ch == t[left]:
                print(f"{ch} == {ch}")
                left += 1

        # after the loop, len(s[left:]) will be the remaining characters
        # to append

        # this means that s is also a subsequence of t
        if left == len(t):
            return 0

        return len(t[left:])