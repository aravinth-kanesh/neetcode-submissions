class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        if len(s) == 1:
            return s

        # start and end indices of current longest palindrome
        start = end = 0

        def expand(left, right):
            """helper function to expand a substring from its centre
            while it is still a palindrome. Also check that left and
            right are within bounds of the string. Returns the final
            indices of left and right"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # when the while loop terminates, left and right pointers
            # are one step too far
            return left + 1, right - 1

        for i in range(len(s)):
            # find length of longest odd-length palindrome
            l1, r1 = expand(i, i)

            # find length of longest even-length palindrome
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]