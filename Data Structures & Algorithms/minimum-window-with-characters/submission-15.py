class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, t_count = defaultdict(int), Counter(t)
        have, need = 0, len(t_count)
        res, res_len = "", float('inf')

        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in t_count and window[left_char] == t_count[left_char] - 1:
                    have -= 1

                left += 1

        return res