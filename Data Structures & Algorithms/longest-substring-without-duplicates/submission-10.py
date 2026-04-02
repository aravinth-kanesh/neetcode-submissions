class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "longest substring" -> variable sliding window
        # for this, initialise left and right pointers
        # keep expanding the window whilst all chars in the window
        # are unique
        # when and if encountering a duplicate char, shrink the 
        # window from the left until it becomes valid again
        # track the longest substring throughout
        left = longest = 0

        # store unique chars in the window
        window = set()

        for right in range(len(s)):
            # window is invalid, shrink from left
            while s[right] in window:
                window.remove(s[left])
                left += 1 # increment left

            # add character at right
            window.add(s[right])

            # update length
            longest = max(longest, right - left + 1)

        return longest
            