class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # return early for such edge cases
        if not s or not t:
            return ""

        # create frequency map for current window and t
        window, freq_map = defaultdict(int), dict(Counter(t))

        # need = number of unique characters in t
        have, need = 0, len(freq_map)

        # store the index range of current minimum and length
        res, res_length = [-1, -1], float('infinity')

        # initialise sliding window
        left = 0
        for right in range(len(s)):
            # extend window to char at right pointer
            ch = s[right]
            window[ch] += 1

            # check if have can be incremented
            if ch in freq_map and window[ch] == freq_map[ch]:
                have += 1

            # try to shrink window while valid to find smaller min
            while have == need:
                # check if current window is local min
                if (right - left + 1) < res_length:
                    res_length = right - left + 1
                    res = [left, right]

                # shrink window from left
                ch = s[left]
                window[ch] -= 1

                # check if window is no longer valid
                if ch in freq_map and window[ch] < freq_map[ch]:
                    have -= 1

                # increment left pointer
                left += 1

        # get index range of min window from res
        left, right = res
        return s[left: right + 1] if res_length != float('infinity') else ""
