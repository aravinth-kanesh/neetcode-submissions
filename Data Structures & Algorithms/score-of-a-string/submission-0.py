class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        n = len(s)

        for i in range(n - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))

        return score