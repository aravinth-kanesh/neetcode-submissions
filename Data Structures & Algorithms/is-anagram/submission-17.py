class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list, t_list = {}, {}

        for ch in s:
            s_list[ch] = s_list[ch] + 1 if ch in s_list else 0
        for ch in t:
            t_list[ch] = t_list[ch] + 1 if ch in t_list else 0

        return s_list == t_list