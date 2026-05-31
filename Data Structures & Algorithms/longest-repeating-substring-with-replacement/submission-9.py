class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # track frequencies of chars in current window
        window = defaultdict(int) # char -> freq

        # track highest frequency in the window, initially 0
        max_freq = 0

        longest = 0 # the answer we are returning

        """The approach: keep expanding the window to the right while window size
        - max_freq <= k. This means <= k replacements are needed for the 
        substring to be only one distinct character. When more than k replacements
        are needed, shrink the window from the left until it is valid again"""

        # initialise sliding window
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            max_freq = max(window.values())

            while (right - left + 1) - max_freq > k:
                window[s[left]] -= 1
                max_freq = max(window.values())
                left += 1

            longest = max(longest, right - left + 1)

        return longest