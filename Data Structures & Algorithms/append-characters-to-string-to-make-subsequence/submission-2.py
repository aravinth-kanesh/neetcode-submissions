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

        # time - loop through each character in s - O(n), where n is the
        # length of s. Worst case is O(n + m)

        # space - O(1), just using left variable