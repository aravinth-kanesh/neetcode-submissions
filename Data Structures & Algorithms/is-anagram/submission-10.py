class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}

        for ch in s:
            count_s[ch] = 1 + count_s.get(ch, 0) 

        for ch in t:
            if ch not in count_s:
                return False

            count_s[ch] -= 1

        for ch in count_s:
            # could have more or less characters than needed
            if count_s[ch] != 0:
                return False

        return True