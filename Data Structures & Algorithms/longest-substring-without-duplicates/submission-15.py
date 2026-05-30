class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = set() # unique characters in current window

        # sliding window approach - extend window from the right until a valid
        # substring found, and then shrink from the left while valid.
        left = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left]) # remove from left until char at s[right] no longer in window.
                left += 1

            # now s[right] is not in the window - add it.
            window.add(s[right])

            # window is valid - compute length and see if answer needs updating.
            longest = max(longest, right - left + 1)

        return longest

