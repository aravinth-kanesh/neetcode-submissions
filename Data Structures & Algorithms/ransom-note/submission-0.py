class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom, mag = [0] * 26, [0] * 26

        for ch in ransomNote:
            ransom[ord(ch) - ord('a')] += 1
        for ch in magazine:
            mag[ord(ch) - ord('a')] += 1

        for ch in set(ransomNote):
            idx = ord(ch) - ord('a')

            if mag[idx] < ransom[idx]:
                return False

        return True