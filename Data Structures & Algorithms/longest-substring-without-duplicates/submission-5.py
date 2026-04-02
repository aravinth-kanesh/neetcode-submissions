class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """To clarify, need to find substrings of the input string
        that have no duplicate characters, and then return the length
        of the longest one. Is that correct?"""

        """Questions to ask for clarification: What are the input
        constraints? Can I assume the input string only consists of
        lower case characters? Which edge cases should I check for?
        Empty input string? Input string with only one character?
        Input string consisting of only the same character? Should
        I optimise my solution to be able to hand really large strings?
        """

        """Brute force solution - find all possible substrings, but this
        is O(n^2) time complexity which is inefficient. A better solution
        would be to use the sliding window approach. I would "shift" the
        sliding window until I find a substring without repeating 
        characters, and then keep expanding it to find a longer one. I would
        use a set to store the characters in the current window, and use this
        to check if new characters are non-repeating. The reason for using a
        set over a list is because checking for membership is more efficient
        - O(1) compared to O(n). This is a much better solution than the brute
        force one since the time complexity is O(n), which is optimal for this
        problem"""

        longest = 0 # variable to store the length of the longest substring found
        window = set() # set to store the characters currently in the window

        # initialise sliding window approach

        left = 0 # left of the sliding window
        for right in range(len(s)): # iterate through every character in the input string
            # shrink the window from the left to ensure window is contiguous
            # shrink the window until it is valid again
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # now that the current window is valid, extend it to the character
            # to the right of the window
            window.add(s[right])
            # check if the new window is the longest one found
            longest = max(longest, right - left + 1)

        return longest
