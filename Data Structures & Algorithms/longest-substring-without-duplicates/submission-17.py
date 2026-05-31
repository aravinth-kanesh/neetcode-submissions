class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = set()

        left = 0
        for right in range(len(s)):
            # shrink window from left until valid again
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # add char at right to the window (window is valid now)
            window.add(s[right])

            # update longest
            longest = max(longest, right - left + 1)

        return longest