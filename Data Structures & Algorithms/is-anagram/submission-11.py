class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}

        for ch in s:
            count_s[ch] = 1 + count_s.get(ch, 0) 

        for ch in t:
            count_t[ch] = 1 + count_t.get(ch, 0)

        return count_s == count_t