class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # create hashmaps for frequencies of s and t
        map_s, map_t = {}, {}

        # populate the t hashmap
        for ch in t:
            map_t[ch] = 1 + map_t.get(ch, 0)

        # res stores the indices of the minimum window
        # res_len stores the length of the min window
        res, res_len = [-1, -1], float("infinity")

        # have is 0
        # need is how many unique characters we have to reach the
        # required count for
        have, need = 0, len(map_t)

        # initialise sliding window
        left = 0
        for right in range(len(s)):
            # add character at right position to window
            char = s[right]
            map_s[char] = 1 + map_s.get(char, 0)
            if char in map_t and map_s[char] == map_t[char]:
                have += 1

            # shrink window
            while have == need:
                # update res and res_len incase current window is min
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                char = s[left]
                map_s[char] -= 1
                # decrement have if condition no longer met
                if char in map_t and map_s[char] < map_t[char]:
                    have -= 1
                # increment left pointer
                left += 1

        left, right = res
        return s[left : right + 1] if res_len != float("infinity") else ""
