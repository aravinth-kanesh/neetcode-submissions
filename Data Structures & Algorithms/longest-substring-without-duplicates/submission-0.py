class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = set()
        left = longest = 0

        for right in range(len(s)):
            while s[right] in current_substring:
                current_substring.remove(s[left])
                left += 1
            
            current_substring.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
