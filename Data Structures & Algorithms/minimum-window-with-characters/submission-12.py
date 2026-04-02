class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # return early for edge cases
        if not s or not t:
            return ""
        
        freq_map = [0] * 52

        # build frequency map for t
        for ch in t:
            freq_map[ord(ch) - ord('a')] += 1

        have = 0

        # count how many unique characters in t
        need = len(set(t))

        # frequency map for the current window
        window = [0] * 52

        # res stores the index ranges of current min window substring
        # res_length set to inf so that first valid substring will be
        # less than it
        res, res_length = [-1, -1], float('infinity')

        # initialise sliding window
        left = 0
        for right in range(len(s)):
            # extend window to character at right pointer
            ch = s[right]
            window[ord(ch) - ord('a')] += 1

            # have the required occurrence of a specific character
            if window[ord(ch) - ord('a')] == freq_map[ord(ch) - ord('a')]:
                have += 1

            # try to shrink window to find minimum when valid
            while have == need:
                # check if current window is local minimum
                if (right - left + 1) < res_length:
                    # update res and res_length
                    res_length = right - left + 1
                    res = [left, right]

                # shrink window from left
                ch = s[left]
                window[ord(ch) - ord('a')] -= 1
                
                # check if window no longer valid 
                if window[ord(ch) - ord('a')] < freq_map[ord(ch) - ord('a')]:
                    have -= 1

                # increment left
                left += 1

        left, right = res
        return s[left: right + 1] if res_length != float('infinity') else ""

        