class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # impossible
        if len(s) < len(t):
            return ""

        count_t = Counter(t)
        window = defaultdict(int) # char -> freq

        have = 0
        need = len(count_t) # number of unique chars whose frequency
        # must be matched or exceeded

        res = [-1, -1] # placeholder for now (left, right)
        res_len = float('inf') # first valid substring will be less than it

        # initialise sliding window
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            # check if condition met
            if char in count_t and window[char] == count_t[char]:
                have += 1

            # if window valid, shrink from left
            while have == need:
                print(s[left:right + 1])
                # update result and result length
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = [left, right]

                left_char = s[left]
                window[left_char] -= 1

                # check if window no longer valid
                if left_char in count_t and window[left_char] == count_t[left_char] - 1:
                    have -= 1

                left += 1

        left, right = res
        return s[left:right + 1] if res_len != float('inf') else ""

        