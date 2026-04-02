class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # check equality after skipping over non-alnum chars

            if s[left].lower() != s[right].lower():
                print(s[left], s[right])
                return False

            left += 1
            right -= 1

        return True