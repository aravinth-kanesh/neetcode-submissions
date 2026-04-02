class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        map_t, window = dict(Counter(t)), defaultdict(int)
        have, need = 0, len(map_t)
        res, res_length = [-1, -1], float('infinity')

        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in map_t and window[s[right]] == map_t[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < res_length:
                    res_length = right - left + 1
                    res = [left, right]

                window[s[left]] -= 1
                if s[left] in map_t and window[s[left]] < map_t[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left: right + 1] if res_length != float('infinity') else ""