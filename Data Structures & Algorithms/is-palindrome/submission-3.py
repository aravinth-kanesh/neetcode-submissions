class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_st = "".join(ch.lower() for ch in s if ch.isalnum())

        left, right = 0, len(final_st) - 1
        while left <= right:
            if final_st[left] != final_st[right]:
                return False
            left += 1
            right -= 1

        return True
