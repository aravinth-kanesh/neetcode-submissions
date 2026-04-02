from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge cases where either string is empty
        if not s or not t:
            return ""

        # I will use a hashmap to count frequencies of each char in t
        # Can use Counter for this for ease and efficiency
        # maps char --> frequency
        map_t = dict(Counter(t))

        # frequency is an integer
        # hashmap to represent current substring of s
        # needs to be a variable size window, not fixed
        window = defaultdict(int)

        # dummy values to store current result range, as not found yet
        # we need to find minimum res_len so set it to pos inf
        # initially, so that any valid substring will be smaller
        res, res_len = [-1, -1], float('infinity')

        # we need a way to track if the substring meets the condition:
        # this is when it has every character in t, and when the
        # frequencies of both characters are the same
        # represent this with have and need variables
        # need is how many characters should be in the substring (and
        # of the same frequencies)
        have, need = 0, len(map_t)

        left = 0
        for right in range(len(s)):
            # add char at right to the current window
            char = s[right]
            window[char] += 1
            # check if we can increment have:
            # when same char in t and frequencies are the same
            if char in map_t and window[char] == map_t[char]:
                have += 1

            # check if window is now valid - when have == need
            # try to shrink valid window to find min valid window
            while have == need:
                # check if we found a new minimum
                # length of current window is right - left + 1
                if (right - left + 1) < res_len:
                    # update the result length
                    res_len = right - left + 1
                    # update the result
                    res = [left, right]

                # shrink window from left
                char = s[left]
                window[char] -= 1

                # check if a condition is no longer met:
                # when char at left is in t and now frequencies
                # are not the same
                if char in map_t and window[char] < map_t[char]:
                    # window is no longer valid
                    have -= 1

                # increment left pointer
                left += 1

        # get left and right bounds from res var
        left, right = res
        # it may be the case that a valid substring was never found
        # in that case, return the empty string
        return s[left:right + 1] if res_len != float('infinity') else ""