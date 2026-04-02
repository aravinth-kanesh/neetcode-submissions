class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, map_t = {}, {}

        for ch in t:
            map_t[ch] = 1 + map_t.get(ch, 0) 

        res, res_len = [-1, -1], float("infinity")
        have, need = 0, len(map_t)

        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] = 1 + window.get(ch, 0)
            if ch in map_t and window[ch] == map_t[ch]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                ch = s[left]
                window[ch] -= 1
                if ch in map_t and window[ch] < map_t[ch]:
                    have -= 1
                left += 1

        left, right = res
        return s[left : right + 1] if res_len != float("infinity") else ""