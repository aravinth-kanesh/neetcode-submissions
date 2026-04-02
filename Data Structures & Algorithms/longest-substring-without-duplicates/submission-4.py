class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = longest = 0

        for right in range(len(s)):
            # shrink window from left while invalid
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # character at right is now unique in the substring
            window.add(s[right])
            # update longest
            longest = max(longest, right - left + 1)

        return longest