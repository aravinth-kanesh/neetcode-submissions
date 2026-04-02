class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            count[ord(ch) - ord('a')] -= 1

            if count[ord(ch) - ord('a')] < 0:
                return False

        return True