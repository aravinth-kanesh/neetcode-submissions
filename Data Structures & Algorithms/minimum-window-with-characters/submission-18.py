class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = Counter(t)
        window = defaultdict(int)

        have = 0
        need = len(count_t)

        res = [-1, -1]
        res_len = float('inf')

        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = [left, right]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in count_t and window[left_char] == count_t[left_char] - 1:
                    have -= 1

                left += 1

        left, right = res
        return s[left:right + 1] if res_len != float('inf') else ""