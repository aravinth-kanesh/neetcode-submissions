class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        if len(s) == 1:
            return s

        start = end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):
            left_odd, right_odd = expand(i, i)
            left_even, right_even = expand(i, i + 1)

            if right_odd - left_odd > end - start:
                start, end = left_odd, right_odd
            if right_even - left_even > end - start:
                start, end = left_even, right_even

        return s[start:end + 1]